import IO_module
import sys

def main():
    args = IO_module.get_arguments()
    try:
        args.func(args)
    except AttributeError:
        print("Too few arguments")

if __name__ == "__main__":
    main()
