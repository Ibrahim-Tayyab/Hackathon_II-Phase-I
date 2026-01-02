# TODO_APP_WITH_I_T (PHASE 1)

Welcome to **TODO_APP_WITH_I_T**, a powerful and efficient task management tool for your terminal.

## 🚀 How to Run

1.  Make sure you are in the project root directory (`e:\Hackathon_II-Phase-I3`).
2.  Run the application using `uv`:

    ```bash
    uv run -m todo_app_with_i_t.main
    ```

## 🎮 How to Use

The application supports both **Interactive Mode** and **Power User Mode** (One-Line Commands).

### Commands Overview

| Command | Shortcut | Description |
| :--- | :--- | :--- |
| **Add** | `A` | Add a new task to your list |
| **List** | `L` | View all tasks with their ID and status |
| **Complete** | `C` | Mark a task as complete |
| **Update** | `U` | Update a task's description |
| **Delete** | `D` | Permanently remove a task |
| **Help** | `H` | Show the help menu |
| **Exit** | `E` | Exit the application |

### Power User Mode (One-Line Commands)

You can save time by typing the command and its details in a single line!

#### Adding a Task
Type `A` followed by your task description.
> `A Buy Milk`
> `Add Finish the report`

#### Marking as Complete
Type `C` followed by the Task ID.
> `C 1`
> `Complete 5`

#### Updating a Task
Type `U` followed by the Task ID. You will be prompted for the new description.
> `U 1`
*Alternatively, you can try `U 1 New Description` (experimental).*

#### Deleting a Task
Type `D` followed by the Task ID.
> `D 1`
> `Delete 2`

### Interactive Mode

If you prefer, you can just type the command letter (e.g., `A`) and press Enter. The app will guide you through the next steps.

---
**Enjoy your productive day with Prime Console App!** 🚀
