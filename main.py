tasks = []

def addTask():
  task = input("Please enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")


def listTasks():
  if not tasks:
    print("No tasks avaliable.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task n°{index} - {task}")


def deleteTask():
  print("----------------------------")
  listTasks()
  try:
    print("----------------------------")

    taskToDelete = int(input("Enter the n° to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task n°{taskToDelete} was not found.")
  except:
    print("Invalid input.")


if __name__ == "__main__":
  ### Create a loop to run the app
  print("Welcome to :")
  print ("-----     ------        --------   -----------  | ")
  print ("|    \    |    |           |            |       | ")       
  print ("|     |   |    |           |            |       | ")         
  print ("|    /    |    |           |            |       | ")     
  print ("-----     ------        --------        |       0 ") 
  print("Do It! is a To Do App, that helps you organize tasks.")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1 - New task")
    print("2 - Delete a task")
    print("3 - List all tasks")
    print("4 - Quit")
    print("----------------------------")
    choice = input("Enter your choice: ")


    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      listTasks()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")

  print(" Goodbye!! ")
                        
