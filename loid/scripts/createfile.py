import os

def create_md_file(filename):
    # Add ".md" to the filename
    md_filename = filename + ".md"

    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)

    # Specify the relative path for the drafts folder
    drafts_folder = os.path.join(current_dir, "../drafts")

    # Create the drafts folder if it doesn't exist
    if not os.path.exists(drafts_folder):
        os.makedirs(drafts_folder)

    # Construct the full path for the Markdown file
    md_filepath = os.path.join(drafts_folder, md_filename)

    # Create an empty Markdown file
    with open(md_filepath, 'w') as md_file:
        pass  # This line does nothing, creating an empty file

    print(f"Empty Markdown file '{md_filename}' created in the 'drafts' folder.")