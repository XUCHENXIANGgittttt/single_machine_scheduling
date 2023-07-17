import tkinter as tk
from tkinter import scrolledtext
import sys
from threading import Thread
import builtins
from product_class import *


class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget
        # backup
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr

    def write(self, str):
        '''
        self.text_space.delete(0.0, tk.END)
        self.text_space.insert(tk.END, "\n" + str)
        self.text_space.insert(tk.END, '\n')
        self.text_space.see(tk.END)
        '''
        self.text_space.insert(tk.END, str)
        self.text_space.see(tk.END)
        # refresh display
        self.text_space.update()

    def restoreStd(self):
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak

    def flush(self):
        pass



def run_program():
    current_year = int(year_entry.get())
    next_week = int(week_entry.get())
    B_max_time = int(B_entry.get())
    A_max_time = int(A_entry.get())

    status_label.config(text="Loading")
    # Create a thread to execute the program
    t = Thread(target=run_program_worker(current_year, next_week, B_max_time, A_max_time))
    t.start()

def run_program_worker(current_year, next_week, B_max_time, A_max_time):
    # Redirecting print output to a text box

    output = sys.stdout  # Secondary backup
    sys.stdout = StdoutRedirector(result_text)

    next_week_index = 'Y23W' + "%02d" % next_week
    file_path = 'main_data.xlsx'
    products = import_products_from_excel(file_path)
    families = classify_into_families(products)

    filtered_products = filter_products_by_family(products, next_week_index)

    filtered_products_B, filtered_products_A = classify_processing_machine(filtered_products)

    consuming_time_B = extract_consuming_time(filtered_products_B, next_week_index)
    consuming_time_A = extract_consuming_time(filtered_products_A, next_week_index)
    consuming_time_B = [builtins.round(num, ndigits=None) for num in consuming_time_B]
    consuming_time_A = [builtins.round(num, ndigits=None) for num in consuming_time_A]
    # Calculating the Changeover Time Matrix
    changeover_matrix_B = calculate_changeover_matrix_B(filtered_products_B)
    changeover_matrix_A = calculate_changeover_matrix_A(filtered_products_A)

    msol_B = plan_optimizer(consuming_time_B, filtered_products_B, changeover_matrix_B)
    msol_A = plan_optimizer(consuming_time_A, filtered_products_A, changeover_matrix_A)

    result_text.delete("1.0", tk.END)  # Empty text box

    print("Solution for Machine B: ")
    msol_B.write()
    # Solve time
    print('Solve time required for this solution: {}'.format(msol_B.get_solve_time()))
    # Total time
    total_time_B = msol_B.get_objective_value()
    print("Optimized consuming time: {} minutes".format(total_time_B))

    if total_time_B <= B_max_time:
        pass
    elif total_time_B > B_max_time:
        print('The consuming time of the Machine B plan has exceeded the max time you give.')
        print('The max time you give for Machine B: {}'.format(B_max_time))
        print('The consuming time of the Machine B plan: {}'.format(total_time_B))

    print()
    print("Solution for Machine A: ")
    msol_A.write()

    print('Solve time required for this solution: {}'.format(msol_A.get_solve_time()))

    total_time_A = msol_A.get_objective_value()
    print("Optimized consuming time: {} minutes".format(total_time_A))

    if total_time_A <= A_max_time:
        pass
    elif total_time_A > A_max_time:
        print('The consuming time of the Machine A plan has exceeded the max time you give.')
        print('The max time you give for Machine A: {}'.format(A_max_time))
        print('The consuming time of the Machine A plan: {}'.format(total_time_A))

    target_B = return_target(msol_B)
    target_A = return_target(msol_A)
    print()
    print('Machine B Sequence = {}'.format(target_B))
    print()
    print('Machine A Sequence = {}'.format(target_A))

    plan_to_excel_B(target_B, products, next_week, next_week_index, current_year)
    plan_to_excel_A(target_A, products, next_week, next_week_index, current_year)

    # Update status text when run is complete
    status_label.config(text="Program Finished")

    sys.stdout = output  # reset


def update_loading_text():
    if status_label.cget("text") == "Loading...":
        status_label.config(text="Loading")
    elif status_label.cget("text") == "Loading..":
        status_label.config(text=status_label.cget("text") + ".")
    elif status_label.cget("text") == "Loading.":
        status_label.config(text=status_label.cget("text") + ".")
    elif status_label.cget("text") == "Loading":
        status_label.config(text=status_label.cget("text") + ".")

    # Timed text update, here set to every 500 milliseconds
    status_label.after(500, update_loading_text)

# Create the Main Window
window = tk.Tk()
window.title("Scheduling")

# Create labels and input boxes
year_label = tk.Label(window, text="Current Year")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

week_label = tk.Label(window, text="Which week you want to plan production?")
week_label.pack()
week_entry = tk.Entry(window)
week_entry.pack()

HCS_label = tk.Label(window, text="Max time for Machine B")
HCS_label.pack()
B_entry = tk.Entry(window)
B_entry.pack()

AIS_label = tk.Label(window, text="Max time for Machine A")
AIS_label.pack()
A_entry = tk.Entry(window)
A_entry.pack()

# Create a run button
run_button = tk.Button(window, text="Run", command=run_program)
run_button.pack()

# Create Runtime Status Text Labels
status_label = tk.Label(window, text="Waiting to run")
status_label.pack()

# Create a result text box
result_text = scrolledtext.ScrolledText(window)
result_text.pack(expand=True, fill=tk.BOTH)

# Initiate timed text updates
update_loading_text()

# Enter the main loop.
window.mainloop()
