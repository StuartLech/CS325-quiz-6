# Logger.py
class Logger:
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Log: {message}")

class FileLogger(Logger):
    def log(self, message):
        print(f"File Log: {message}")  # Simulate file logging

# Application.py
class Application:
    def __init__(self, logger):
        self.logger = logger

    def do_something(self):
        self.logger.log("Application doing something")

# main function
def main():
    logger = ConsoleLogger()  # Or FileLogger(), or any other Logger
    app = Application(logger)
    app.do_something()

if __name__ == "__main__":
    main()
