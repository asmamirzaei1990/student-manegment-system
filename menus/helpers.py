from exceptions import AppError

def run_action(action):
    try:
        action()
    except AppError as exc:
        print(f"Error: {exc}")
    except ValueError:
        print("Error: invalid input format.")
