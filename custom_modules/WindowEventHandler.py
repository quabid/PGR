from .CoordinatesManager import save_location, get_location


def on_open(content):
    win_coordinates = get_location()
    x = None
    y = None
    if win_coordinates:
        x = win_coordinates['x']
        y = win_coordinates['y']
        content.geometry("+{}+{}".format(x, y))




def config_location(content):

    coordinates = {
        'x': content.winfo_rootx(),
        'y': content.winfo_rooty()
    }
    save_location(coordinates)
    content.destroy()


def handle(window):

    def on_close():
        coordinates = {
            'x': window.winfo_rootx(),
            'y': window.winfo_rooty()
        }
        save_location(coordinates)
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    on_open(window)
