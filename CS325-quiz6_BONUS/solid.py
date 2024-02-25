from abc import ABC, abstractmethod
from typing import List

# Observer pattern interfaces
class Observer(ABC):
    @abstractmethod
    def update(self, activity):
        pass

class Observable(ABC):
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, activity):
        for observer in self.observers:
            observer.update(activity)

# SRP: User class focuses solely on user-related information
class User:
    def __init__(self, name):
        self.name = name

# SRP: Activity class focuses on activity-related data
class Activity(ABC):
    def __init__(self, type, duration, distance):
        self.type = type
        self.duration = duration
        self.distance = distance

    @abstractmethod
    def calculate_calories(self):
        pass

# ISP: Separate interfaces for collection and display
# OCP & LSP: ActivityMonitor collects data and is extendable for new activities
class ActivityMonitor(Observable):
    def __init__(self, storage, display):
        super().__init__()
        self.storage = storage
        self.add_observer(display)

    def log_activity(self, activity: Activity):
        self.storage.store(activity)
        self.notify_observers(activity)

# DIP: DataStorage is injected, allowing for different storage implementations
class DataStorage:
    def __init__(self):
        self.activities = []

    def store(self, activity: Activity):
        self.activities.append(activity)
        print(f"Stored {activity.type} activity.")

# DIP: Display is injected, decoupling the display mechanism
class Display(Observer):
    def update(self, activity):
        print(f"New activity recorded: {activity.type}, Duration: {activity.duration}, Distance: {activity.distance}")

# Example concrete activity
class Running(Activity):
    def calculate_calories(self):
        return self.duration * 10  # Simplified calorie calculation

# Main function to demonstrate functionality
def main():
    user = User("John Doe")
    storage = DataStorage()
    display = Display()
    monitor = ActivityMonitor(storage, display)

    running_activity = Running("Running", 30, 5)
    monitor.log_activity(running_activity)

if __name__ == "__main__":
    main()
