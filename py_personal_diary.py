import os
import datetime
import pickle

class DiaryEntry:
    def __init__(self, date, content):
        self.date = date
        self.content = content

class PersonalDiary:
    def __init__(self):
        self.entries = []

    def add_entry(self, content):
        current_date = datetime.datetime.now()
        entry = DiaryEntry(current_date, content)
        self.entries.append(entry)
        print("Diary entry added successfully!")

    def view_entries(self):
        if not self.entries:
            print("No entries found.")
        else:
            for idx, entry in enumerate(self.entries, start=1):
                print(f"Entry {idx} - Date: {entry.date}, Content: {entry.content}")

    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.entries, file)
        print("Diary entries saved to file.")

    def load_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                self.entries = pickle.load(file)
            print("Diary entries loaded from file.")
        except FileNotFoundError:
            print("No saved entries found.")

    def search_entries(self, keyword):
        matching_entries = [entry for entry in self.entries if keyword.lower() in entry.content.lower()]
        if matching_entries:
            print(f"Entries matching '{keyword}':")
            for idx, entry in enumerate(matching_entries, start=1):
                print(f"Entry {idx} - Date: {entry.date}, Content: {entry.content}")
        else:
            print("No matching entries found.")

def main():
    diary = PersonalDiary()

    while True:
        print("\nPyPersonalDiary - Your Digital Diary")
        print("1. Add Diary Entry")
        print("2. View Diary Entries")
        print("3. Save Entries to File")
        print("4. Load Entries from File")
        print("5. Search Entries by Keyword")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            content = input("Enter your diary entry: ")
            diary.add_entry(content)

        elif choice == "2":
            print("\nDiary Entries:")
            diary.view_entries()

        elif choice == "3":
            filename = input("Enter the filename to save: ")
            diary.save_to_file(filename)

        elif choice == "4":
            filename = input("Enter the filename to load: ")
            diary.load_from_file(filename)

        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            diary.search_entries(keyword)

        elif choice == "6":
            print("Exiting PyPersonalDiary. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
