queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
  """Print everyone currently in the queue"""
  print()
  print("Current queue:")
  print()
  for i, singer in enumerate(queue):
    name, song = singer
    print(f"{i + 1 }. {name} - {song}")
  print()
  print("Options:  add / next / remove / quit")

def prompt_for_singer():
  """Ask for a name and a song, and return them cleaned up."""
  name = input("Name: ").strip().title()
  song = input("Song: ").strip().title()
  return name, song

def add_singer(queue):
  """Ask for the singer and add them to the queue"""
  name, song = prompt_for_singer()
  queue.append((name, song))
  print()
  print(f"Added {name} to the queue.")

def next_singer(queue):
  """Announce the next singer in the queue"""
  new_singer = queue.pop(0)
  name, song = new_singer
  print(f"\nNow up: {name} - {song}")

def remove_singer(queue): 
  """Remove singer fron the queue"""
  name = input("\nWho do you want to remove? ").strip().title()
  for singer in queue:
    singer_name = singer[0]  # Extract the name from the tuple
    if(singer_name == name):
       queue.remove(singer)
       print(f"\n{name} has been removed from the queue.")
       return
  print(f"\n{name} is not in the queue.")

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
      elif command == "remove":
        remove_singer(queue)
      elif command == "next":
        next_singer(queue)
      else: 
        print(f"Sorry, I don't know the command '{command}'")

run_app(queue)
