def center_window(root, width, height):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the geometry of the window
    root.geometry(f'{width}x{height}+{x}+{y}')

def root_size (root,column_names) :
    if len(column_names) == 1 :
        center_window(root, 400, 219)
        return 119
    elif len(column_names) == 2 :
        center_window(root, 400, 267)
        return 167
    elif len(column_names) == 3 :
        center_window(root, 400, 317)
        return 217
    elif len(column_names) == 4:
        center_window(root, 400, 367)
        return 267
    else :
        center_window(root, 400, 370)
        return 370
