katz_deli = []
eugene_deli = ["Eugene", "Enegue"]

def line(the_line):
    counter=0
    current_line=[]
    line_message=("The line is currently:")
    if not the_line:
        line_message=("The line is currently empty.")
    else:
        while counter <= (len(the_line)-1):
            line_message+=f' {counter+1}. '
            line_message+=f'{the_line[counter]}'
            counter+=1
    print(f'{line_message}')

line(eugene_deli)
    
def take_a_number(the_line, customer_name):
    the_line.append(customer_name)
    if len(the_line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f'Welcome, {customer_name}. You are number {len(the_line)} in line.')
    
def now_serving(a_deli):
    if not a_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {a_deli[0]}.')
        a_deli.pop(0)
    
    
now_serving(eugene_deli)