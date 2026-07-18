# Assignment 4
# Part 2: Priority Queue using Binary Max Heap
# Bilal Khalid

# Task Class

class Task:
    # This class represents a single task.

    def __init__(self, task_id, priority, arrival_time, deadline):

        # Unique task ID
        self.task_id = task_id

        # Larger number means higher priority
        self.priority = priority

        # Time when task arrives
        self.arrival_time = arrival_time

        # Deadline of the task
        self.deadline = deadline

    def __str__(self):
        # Display task information.

        return (f"Task ID: {self.task_id}, "
                f"Priority: {self.priority}, "
                f"Arrival: {self.arrival_time}, "
                f"Deadline: {self.deadline}")

# Priority Queue Class

class PriorityQueue:

    def __init__(self):

        # Python list is used as the heap
        self.heap = []

    # Helper Functions

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    # Insert Operation

    def insert(self, task):
        # Add a new task into the heap.

        # Put task at the end
        self.heap.append(task)

        current = len(self.heap) - 1

        # Move upward while parent has lower priority
        while current > 0:

            parent = self.parent(current)

            if self.heap[current].priority > self.heap[parent].priority:

                self.heap[current], self.heap[parent] = \
                    self.heap[parent], self.heap[current]

                current = parent

            else:
                break

    # Heapify Down

    def heapify_down(self, index):

        size = len(self.heap)

        while True:

            largest = index

            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and \
                    self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < size and \
                    self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:

                self.heap[index], self.heap[largest] = \
                    self.heap[largest], self.heap[index]

                index = largest

            else:
                break

    # Extract Maximum

    def extract_max(self):
        # Remove highest-priority task.

        if self.is_empty():
            return None

        highest = self.heap[0]

        last = self.heap.pop()

        if len(self.heap) > 0:

            self.heap[0] = last

            self.heapify_down(0)

        return highest

    # Increase Priority

    def increase_key(self, task_id, new_priority):
        # Increase priority of an existing task.

        for i in range(len(self.heap)):

            if self.heap[i].task_id == task_id:

                if new_priority <= self.heap[i].priority:

                    print("New priority should be larger.")
                    return

                self.heap[i].priority = new_priority

                current = i

                while current > 0:

                    parent = self.parent(current)

                    if self.heap[current].priority > \
                            self.heap[parent].priority:

                        self.heap[current], self.heap[parent] = \
                            self.heap[parent], self.heap[current]

                        current = parent

                    else:
                        break

                return

        print("Task not found.")

    # Check Empty

    def is_empty(self):

        return len(self.heap) == 0

    # Display Heap

    def display(self):

        print("\nCurrent Tasks")

        for task in self.heap:
            print(task)

# Main Program

queue = PriorityQueue()

# Create some sample tasks

task1 = Task(101, 5, "08:00", "12:00")
task2 = Task(102, 9, "08:10", "11:00")
task3 = Task(103, 3, "08:20", "02:00")
task4 = Task(104, 7, "08:30", "01:00")

# Insert tasks

queue.insert(task1)
queue.insert(task2)
queue.insert(task3)
queue.insert(task4)

queue.display()

# Increase priority

print("\nIncreasing priority of Task 103...\n")

queue.increase_key(103, 10)

queue.display()

# Process tasks

print("\nExecuting Tasks\n")

while not queue.is_empty():

    current = queue.extract_max()

    print(current)