import cmd
import argparse

class MyInterpreter(cmd.Cmd):
    prompt = '> '

    def do_hello(self, arg):
        """Greets the user."""
        parser = argparse.ArgumentParser()
        parser.add_argument("name", help="The name of the person to greet")
        args = parser.parse_args(arg.split())
        print("Hello, " + args.name + "!")

    def help_hello(self):
        print("Usage: hello <name>")
        print("Greets the specified person.")

    def do_EOF(self, line):
        """Handles the EOF command (Ctrl+D)."""
        print("Exiting interpreter...")
        return True

    def default(self, line):
        """Handles unknown commands gracefully."""
        print("Unknown command:", line)

interpreter = MyInterpreter()
interpreter.cmdloop()