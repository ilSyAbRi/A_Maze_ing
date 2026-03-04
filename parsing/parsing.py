def check_the_file():
    try:
        x = open("config.txt","r")
    except FileNotFoundError:
        print("Hey! I can’t find config.txt. Did you move it or rename it?")

if __name__ == "__main__":
    check_the_file()
