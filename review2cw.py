# userTask = {
#     "task1" : "clean bathroom",
#     "task2" :"Wash the Dishes",
#     "task3" : "cook breakfast",
#     "task4" :"do laundry",
#     "task5" : "do homework",
#     "task6" :"make the bed"
#
# },


userTask = ["cleanroom", "wash dishes"]       #created an array with two items


def main():             #put everything in my main function
    main_Task()


def main_Task():                   #creating my main function
    asktask1 = ""                   #making an empty string

    while asktask1.lower() != "no":
        menu_Selection = int(input("1.List Task, 2.Add task, 3.Delete Task, 4.Quit\n"))  #provding options for user to select
        if menu_Selection == 1:              #if 1 is selected it will call my list task function
            list_task()
        elif menu_Selection == 2:                 #if 2 is selected it will call my add task function
            add_Task()
        elif menu_Selection == 3:                  #if 3 is selected it will call my delete task function
            delete_Task()
        elif menu_Selection == 4:                  #if 4 is selected it will call my quit function
            quitFunction()
            break
        else:
            print("Not an entry")

# userRequest()
def list_task():                           #this function is iterating through the elements in my array
    for elements in userTask:
        print(elements)



def add_Task():
    task_added = input("what task would you like to add?\n")            #asking user what task they ould like to add
    userTask.append(task_added)
    print(userTask)


def delete_Task():
    for element in userTask:                   #provding a reference to the user before they delete
        print(element)
    task_deleted = input("what task would you like to delete?\n")
    if task_deleted in userTask:
        userTask.remove(task_deleted)
    else:
        print("task not available")

def quitFunction():
    print("Thanks for trying ")              #good bye comment to user if they quit



#     Create a task list.l
#     A user is presented with the text below.
#
#     Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
#     Make each option a different function in your program.
#     Do <strong>NOT</strong> use Google. Do <strong>NOT</strong> use other students. Try to do this on your own.
#
# ```
# Congratulations! You're running [YOUR NAME]'s Task List program.
#
# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program
if __name__ == '__main__':
    main()