import sys
from todo_app_with_i_t.services.task_service import TaskService

class CLIHandler:
    def __init__(self):
        self.service = TaskService()

    def print_header(self):
        print("\n" + "="*50)
        print("          TODO_APP_WITH_I_T (PHASE 1)         ")
        print("        Created by Ibrahim Memon              ")
        print("    https://github.com/Ibrahim-Tayyab         ")
        print("="*50 + "\n")

    def print_menu(self):
        print("MAIN MENU")
        print("[A]dd Task")
        print("[L]ist Tasks")
        print("[C]omplete Task")
        print("[U]pdate Task")
        print("[D]elete Task")
        print("[E]xit")

    def run(self):
        self.print_header()
        while True:
            self.print_menu()
            user_input = input("\nEnter choice (H for Help) > ").strip()
            
            if not user_input:
                continue

            parts = user_input.split(maxsplit=1)
            command = parts[0].upper()
            args = parts[1] if len(parts) > 1 else None

            if command in ['A', 'ADD']:
                self.handle_add(args)
            elif command in ['L', 'LIST']:
                self.handle_list()
            elif command in ['C', 'COMPLETE']:
                self.handle_complete(args)
            elif command in ['U', 'UPDATE']:
                self.handle_update(args)
            elif command in ['D', 'DELETE']:
                self.handle_delete(args)
            elif command in ['E', 'EXIT']:
                print("Goodbye!")
                sys.exit(0)
            elif command in ['H', 'HELP']:
                 self.print_help()
            else:
                print("Invalid choice. Please try again.")
            
            print("-" * 30)

    def print_help(self):
        print("\nHELP MANUAL")
        print("You can select a command, or type the command followed by arguments.")
        print("Examples: 'A Buy Milk', 'C 1', 'D 2'")
        print("-" * 30)
        print("A or ADD      - Add a new task")
        print("L or LIST     - View all tasks")
        print("C or COMPLETE - Mark task as complete (usage: C <ID>)")
        print("U or UPDATE   - Update task description (usage: U <ID>)")
        print("D or DELETE   - Delete a task (usage: D <ID>)")
        print("E or EXIT     - Exit the application")

    def handle_add(self, description=None):
        if not description:
            description = input("Enter task description: ").strip()
        
        if description:
            try:
                task = self.service.add_task(description)
                print(f"Task added: [ID: {task.id}] {task.description}")
            except ValueError as e:
                 print(f"Error: {e}")
        else:
            print("Operation cancelled or invalid input.")

    def handle_list(self):
        tasks = self.service.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print(f"{'ID':<5} {'Status':<12} {'Description'}")
            print("-" * 40)
            for task in tasks:
                status_display = f"[{task.status.title()}]"
                print(f"{task.id:<5} {status_display:<12} {task.description}")

    def handle_complete(self, task_id_input=None):
        try:
            if not task_id_input:
                task_id_input = input("Enter Task ID to complete: ")
            
            if not task_id_input.strip():
                return
            
            task_id = int(task_id_input)
            task = self.service.complete_task(task_id)
            if task:
                print(f"Task {task.id} marked as Complete.")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    def handle_update(self, input_args=None):
        try:
            task_id = None
            new_desc = None

            # Attempt to parse "ID Description" from single line input
            if input_args:
                parts = input_args.split(maxsplit=1)
                if parts[0].isdigit():
                    task_id = int(parts[0])
                    if len(parts) > 1:
                        new_desc = parts[1]
            
            # Interactive fallback
            if task_id is None:
                task_id_input = input("Enter Task ID to update: ")
                if not task_id_input.strip():
                    return
                task_id = int(task_id_input)
            
            # Check if task exists
            existing_task = self.service.repository.get(task_id)
            if not existing_task:
                print("Task not found.")
                return

            if new_desc is None:
                new_desc = input(f"Enter new description for '{existing_task.description}': ").strip()

            if new_desc:
                task = self.service.update_task(task_id, new_desc)
                if task:
                    print(f"Task {task.id} updated to: {task.description}")
            else:
                print("Description cannot be empty.")
        except ValueError:
            print("Invalid input.")

    def handle_delete(self, task_id_input=None):
        try:
            if not task_id_input:
                task_id_input = input("Enter Task ID to delete: ")
            
            if not task_id_input.strip():
                return
            
            task_id = int(task_id_input)
            if self.service.delete_task(task_id):
                print(f"Task {task_id} deleted.")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid input.")
