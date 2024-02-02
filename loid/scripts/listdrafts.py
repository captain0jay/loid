import os
import datetime
from tabulate import tabulate

def list_drafts():
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)

    # Specify the relative path for the drafts folder
    drafts_folder = os.path.join(current_dir, "../drafts")

    # Create the drafts folder if it doesn't exist
    if not os.path.exists(drafts_folder):
        os.makedirs(drafts_folder)

    # Check if the drafts folder exists
    if not os.path.exists(drafts_folder):
        print("The 'drafts' folder does not exist.")
        return

    # Get a list of all files in the drafts folder without the .md extension
    draft_files = [file for file in os.listdir(drafts_folder) if file.endswith(".md")]

    if not draft_files:
        print("No Markdown files found in the 'drafts' folder.")
        return

    # Sort the files based on creation time (ascending order)
    draft_files.sort(key=lambda file: os.path.getctime(os.path.join(drafts_folder, file)))

    # Prepare data for tabulation
    table_data = []
    for i, file in enumerate(draft_files, start=1):
        file_path = os.path.join(drafts_folder, file)
        file_without_extension = os.path.splitext(file)[0]
        creation_time = os.path.getctime(file_path)
        modified_time = os.path.getmtime(file_path)
        
        formatted_creation_time = datetime.datetime.fromtimestamp(creation_time).strftime('%d/%m/%y %H:%M')
        formatted_modified_time = datetime.datetime.fromtimestamp(modified_time).strftime('%d/%m/%y %H:%M')
        
        table_data.append([i, file_without_extension, formatted_creation_time, formatted_modified_time])

    # Define headers for the table
    headers = ["Sr. No", "Name", "Creation", "Updation"]

    # Display the table
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Call the function to list drafts
