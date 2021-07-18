from .CoordinatesManager import save_location, get_location


def window_handler(window):

    def on_close():
        print("\n\n\t\tClosing the main window\n\n")
        coordinates = {
            'x': window.winfo_rootx(),
            'y': window.winfo_rooty()
        }
        save_location(coordinates)
        window.destroy()

    def on_open(content):
        print("\n\n\t\tOpening the main window")
        win_coordinates = get_location()
        x = None
        y = None
        if win_coordinates:
            x = win_coordinates['x']
            y = win_coordinates['y']
            content.geometry("+{}+{}".format(x, y))

    window.protocol("WM_DELETE_WINDOW", on_close)
    on_open(window)
