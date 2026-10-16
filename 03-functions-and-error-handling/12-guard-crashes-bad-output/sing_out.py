
queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
    """Print everyone currently in the queue"""
    if len(queue) == 0:
        print("\nThe queue is empty.")
    else:
        print()
        print("Current queue:")
        print()
        for i, singer in enumerate(queue):
            name, song = singer
            print(f"{i + 1}. {name} - {song}")
        print()
    print("Options: add / next / top / remove / quit")


def prompt_for_singer():
    """Ask for a name and a song, and return them cleaned up."""
    name = input("Name: ").strip().title()
    song = input("Song: ").strip().title()
    return name, song


def add_singer(queue):
    """Ask for the singer and add them to the queue"""
    name, song = prompt_for_singer()
    if not name or not song:
        print("Oops! I need a name and a song to add someone to the queue.")
        return
    queue.append((name, song))
    print()
    print(f"Added {name} to the queue.")


def next_singer(queue):
    if len(queue) == 0:
        print("Oops! There's no one left to call up!")
        return

    name, song = queue.pop(0)
    print()
    print(f"NOW UP: {name} - {song}")


def move_to_top(queue):
    position = int(input("Who do you want to move to the top? Enter a number: "))
    if len(queue) == 0:
        print("The queue is empty. There's no one to move to the top.")
        return
    if len(queue) < 2:
        print("You need at least two singers in the queue to move someone to the top.")
        return

    if position < 1 or position > len(queue):
        print("Invalid queue position. Please enter a valid number.")
        return

    print()
    singer = queue.pop(position - 1)
    queue.insert(0, singer)
    name, song = singer
    print(f"Moved {name} to the top of the queue!")


def remove_singer(queue):
    """Remove singer from the queue"""
    if len(queue) == 0:
        print("The queue is empty. There's no one to remove.")
        return

    name = input("Who do you want to remove? ").strip().title()
    print()

    for singer in queue:
        if singer[0] == name:
            queue.remove(singer)
            print(f"Removed {name} from the queue.")
            return

    print(f"There's no one named {name} in the queue.")


def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        command = input("> ")

        if command == "quit":
            is_running = False
            print("The queue is closed. Good night!")
        elif command == "add":
            add_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "top":
            move_to_top(queue)
        elif command == "remove":
            remove_singer(queue)
        else:
            print(f"Sorry, I don't know the command '{command}'")


run_app(queue)
