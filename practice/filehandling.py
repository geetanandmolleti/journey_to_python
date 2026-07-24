pushpa_dialogues = [
    "Pushpa ante flower anukuntiva... fire!",
    "Thaggedhe le!",
    "Idhi Pushpa gaadi rule!",
    "Lokamlo undedhi rende kulaalu... okati unnodu, rendodi lenodu.",
    "Pushpa ni muttaalanna, Pushpa gaadini kottaalanna... gunde dhairyam kaadhu, ontlo raktham unte saripodu, Pushpa gaadi dhaya undaali.",
    "Nuvvu adavilo puttaav... nenu adavini aaladaanki puttaanu.",
]


def write_pushpa():
    # 'w' creates the file or truncates it if exists; write each dialogue on its own line
    with open("pushpa.txt", "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in pushpa_dialogues)
    print("Wrote pushpa.txt")


def append_xyz():
    # 'a' appends to the file (creates if not exists)
    with open("xyz.txt", "a", encoding="utf-8") as f:
        f.write("hello\n")
        # append dialogues with newlines
        f.writelines(line + "\n" for line in pushpa_dialogues)
    print("Appended to xyz.txt")


def read_whole(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    print(f"Contents of {filename} (whole file):\n{data}")


def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"{i}: {line.rstrip()}")


def read_into_list(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"Read {len(lines)} lines into a list from {filename}")
    return lines


def r_plus_example():
    # 'r+' opens for reading and writing without truncating (file must exist)
    fname = "rplus_example.txt"
    # ensure file exists first
    with open(fname, "w", encoding="utf-8") as f:
        f.write("First line\n")

    with open(fname, "r+", encoding="utf-8") as f:
        print("r+ before write, content:")
        print(f.read())
        f.write("Appended via r+\n")  # writes at current pointer (end after read)
    print(f"Updated {fname}")


def w_plus_example():
    # 'w+' truncates or creates, then allows reading/writing
    fname = "gopi.txt"
    with open(fname, "w+", encoding="utf-8") as f:
        f.write("name : isa gopi krishna")
        pos = f.tell()
        print(f"Pointer after write: {pos}")
        f.seek(0)
        print("Content after seek to start:")
        print(f.read())


def a_plus_example():
    # 'a+' opens for append and read; pointer starts at end for writes
    fname = "xyz.txt"
    with open(fname, "a+", encoding="utf-8") as f:
        f.write("hello from a+\n")
        f.seek(0)  # move pointer to start to read whole file
        print(f"Contents of {fname}:")
        print(f.read())


def main():
    write_pushpa()
    append_xyz()

    print("\n--- Read pushpa.txt whole ---")
    read_whole("pushpa.txt")

    print("\n--- Read pushpa.txt line by line ---")
    read_lines("pushpa.txt")

    print("\n--- Read lines into list ---")
    lines = read_into_list("pushpa.txt")
    print(lines[:2])  # show first two items from the list

    print("\n--- r+ example ---")
    r_plus_example()

    print("\n--- w+ example ---")
    w_plus_example()

    print("\n--- a+ example (reads xyz.txt) ---")
    a_plus_example()


if __name__ == "__main__":
    main()



import json
import pickle
import sys


def json_example():
    s = input('Enter JSON data (example: {"name":"gopi", "age":20}): ')
    try:
        a = json.loads(s)
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
        return
    b = json.dumps(a)
    print("Serialized (JSON string):", b, type(b))
    c = json.loads(b)
    print("Deserialized (Python object):", c, type(c))


def pickle_example():
    s = input('Enter JSON data to pickle (example: {"name":"gopi", "age":20}): ')
    try:
        a = json.loads(s)
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
        return

    b = pickle.dumps(a)
    print("Serialized (pickle bytes):", b)

    c = pickle.loads(b)
    print("Deserialized (Python object):", c, type(c))


def main():
    print("Choose example to run:")
    print("1: JSON serialize/deserialize")
    print("2: Pickle serialize/deserialize")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        json_example()
    elif choice == "2":
        pickle_example()
    else:
        print("Invalid choice")
        sys.exit(1)


if __name__ == "__main__":
    main()