from rich import text
from rich import box
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout

from rich.live import Live
from rich.traceback import install
install(show_locals=True)
from rich.console import Console

from datetime import datetime
import numpy as np
import asciichartpy
import csv
import keyboard
from time import sleep
import psutil
import platform

tasks = []

# Add a task to the list
def add_task(task):
    tasks.append(task)

# Delete a task from the list
def delete_task(task):
    tasks.remove(task)

# Update a task in the list
def update_task(old_task, new_task):
    index = tasks.index(old_task)
    tasks[index] = new_task

# Print the list of tasks
def print_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

# Main program loop
while True:
    print(" ")
    print("1. Add task")
    print("2. Delete task")
    print("3. Update task")
    print("4. Print tasks")
    print("5. Quit")
    print(" ")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to delete: ")
        delete_task(task)
    elif choice == "3":
        old_task = input("Enter the task to update: ")
        new_task = input("Enter the new task: ")
        update_task(old_task, new_task)
    elif choice == "4":
        print(" ")
        print_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")