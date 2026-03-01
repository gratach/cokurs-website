import argparse
from pathlib import Path
from json import dump, load
from shutil import rmtree, copytree

default_config = {
    "cokurs-url": "cokurs.example.com",
    "institution-url": "the-institution-that-runs-cokurs.example.com",
    "institution-text": "Enter the name of the institution that runs Cokurs",
}

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Build the cokurs website.")
    
    # Add the --import-folder argument
    parser.add_argument(
        '-i', '--import-folder',
        type=str,
        help='Path to the import folder containing the data of the website. The format of this folder is the same as the folder that is created when running the export_data.py script.',
        required=False
    )
    parser.add_argument(
        '-d', '--dist-folder',
        type=str,
        help='Path to the dist folder where the cokurs website is built. If this argument is not provided, the script will look for a dist folder in the same directory as the script. The content of this folder will be updated when running the build_website.py script. Only existing content that is not compatible with the data in the import folder will be overwritten.',
        required=False
    )
    parser.add_argument(
        '-m', '--metadata-folder',
        type=str,
        help='Path to the metadata folder where the metadata of the website is stored. If this argument is not provided, the script will look for a metadata folder in the same directory as the script. The contents of this folder will be updated when running the build_website.py script. Only existing metadata that is not compatible with the data in the import folder will be overwritten.',
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Access the --import-folder argument
    if args.import_folder:
        print(f"Import folder provided: {args.import_folder}")
        import_path = Path(args.import_folder)
        if not import_path.is_dir():
            print(f"Error: The provided import folder path '{import_path}' is not a directory.")
            return
    else:
        print("No import folder provided.")
        import_path = None

    # Access the --dist-folder argument
    if args.dist_folder:
        print(f"Dist folder provided: {args.dist_folder}")
        dist_path = Path(args.dist_folder)
        # Check if the provided dist folder path is a directory        
        if dist_path.is_dir():
            # Let the user agree to overwrite the content of the dist folder
            confirm = input(f"The provided dist folder path '{dist_path}' already exists. Do you want to overwrite its content? (y/n): ")
            if confirm.lower() != 'y':
                print("Operation cancelled.")
                return
        elif dist_path.exists():
            print(f"Error: The provided dist folder path '{dist_path}' is not a directory.")
            return
        else:
            try:
                dist_path.mkdir(parents=True, exist_ok=True)
                print(f"Created dist folder at: {dist_path}")
            except Exception as e:
                print(f"Error: Could not create dist folder at '{dist_path}'. {e}")
                return
    else:
        print("No dist folder provided.")
        dist_path = Path(__file__).parent / "dist"
        print(f"Using default dist folder: {dist_path}")

    # Access the --metadata-folder argument
    if args.metadata_folder:
        print(f"Metadata folder provided: {args.metadata_folder}")
        metadata_path = Path(args.metadata_folder)
    else:
        print("No metadata folder provided.")
        metadata_path = Path(__file__).parent / "metadata"
        print(f"Using default metadata folder: {metadata_path}")
    if not metadata_path.is_dir():
        try:
            metadata_path.mkdir(parents=True, exist_ok=True)
            print(f"Created metadata folder at: {metadata_path}")
        except Exception as e:
            print(f"Error: Could not create metadata folder at '{metadata_path}'. {e}")
            return
    else:
        print(f"Metadata folder already exists at: {metadata_path}")

    # Load the config.json file from the import folder if it exists
    if import_path:
        import_config_file = import_path / "config.json"
        if import_config_file.is_file():
            print(f"Found config.json in the import folder: {import_config_file}")
            try:
                with import_config_file.open() as f:
                    import_config = load(f)
                print("Loaded config.json successfully.")
            except Exception as e:
                print(f"Error: Could not load config.json. {e}")
        else:
            print(f"No config.json file found in the import folder: {import_path}")
            importconfig = {}
    else:
        print("No import folder provided, skipping config.json loading.")
        import_config = {}

    # Load the config.json file from the metadata folder if it exists
    metadata_config_file = metadata_path / "config.json"
    if metadata_config_file.is_file():
        print(f"Found config.json in the metadata folder: {metadata_config_file}")
        try:
            with metadata_config_file.open() as f:
                metadata_config = load(f)
            print("Loaded config.json successfully.")
        except Exception as e:
            print(f"Error: Could not load config.json. {e}")
    else:
        print(f"No config.json file found in the metadata folder: {metadata_path}")
        metadata_config = {}

    # Update the config.json file in the metadata folder recursively with the data from the config.json file in the import folder if it exists
    updated_metadata_config = default_config.copy()
    updated_metadata_config.update(metadata_config)
    updated_metadata_config.update(import_config)
    try:
        with metadata_config_file.open("w") as f:
            dump(updated_metadata_config, f, indent=4)
        print(f"Updated config.json in metadata folder: {metadata_config_file}")
    except Exception as e:
        print(f"Error: Could not update config.json in metadata folder. {e}")


    # Clear the incompatible content of the dist folder if it exists and create it if it does not exist
    notOverwrittenFileContents = ["glyphr", "sequencer", "website", "scetchio", "svgedit", "bilder", "lsystem", "obj", "fraktal", "piskel"]
    dist_path.mkdir(parents=True, exist_ok=True)
    print(f"Clearing incompatible content of dist folder at: {dist_path}")
    deleted_files_count = 0
    deleted_directories_count = 0
    for item in dist_path.iterdir():
        if item.name in notOverwrittenFileContents:
            print(f"Keeping existing content in dist folder: {item}")
            continue
        if item.is_file():
            try:
                item.unlink()
                deleted_files_count += 1
            except Exception as e:
                print(f"Error: Could not delete file '{item}'. {e}")
        elif item.is_dir():
            try:
                rmtree(item)
                deleted_directories_count += 1
            except Exception as e:
                print(f"Error: Could not delete directory '{item}'. {e}")
    print(f"Deleted {deleted_files_count} files and {deleted_directories_count} directories from dist folder.")

    # Copy the content from the www folder to the dist folder
    www_path = Path(__file__).parent / "www"
    if not www_path.is_dir():
        print(f"Error: The www folder does not exist at '{www_path}'.")
        return
    print(f"Copying content from www folder to dist folder...")
    copied_files_count = 0
    copied_directories_count = 0
    for item in www_path.iterdir():
        dest = dist_path / item.name
        if item.is_file():
            try:
                dest.write_bytes(item.read_bytes())
                copied_files_count += 1
            except Exception as e:
                print(f"Error: Could not copy file '{item}' to '{dest}'. {e}")
        elif item.is_dir():
            try:
                copytree(item, dest)
                copied_directories_count += 1
            except Exception as e:
                print(f"Error: Could not copy directory '{item}' to '{dest}'. {e}")
    print(f"Copied {copied_files_count} files and {copied_directories_count} directories from www folder to dist folder.")

    # Replace the placeholders in the www files with the values from the config.json file in the metadata folder
    print("Replacing placeholders in www files with values from config.json in metadata folder...")
    number_of_occurrences_per_key = {key: 0 for key in updated_metadata_config.keys()}
    number_of_files_that_could_not_be_processed = 0
    for item in dist_path.rglob("*.*"):
        if item.is_file() and not item.name in notOverwrittenFileContents:
            try:
                content = item.read_text()
                for key, value in updated_metadata_config.items():
                    placeholder = f"{{{{{key}}}}}"
                    count = content.count(placeholder)
                    number_of_occurrences_per_key[key] += count
                    content = content.replace(placeholder, value)
                item.write_text(content)
            except Exception as e:
                number_of_files_that_could_not_be_processed += 1
    for key, count in number_of_occurrences_per_key.items():
        if count > 0:
            print(f"Replaced {count} occurrences of placeholder '{{{{{key}}}}}' with value '{updated_metadata_config[key]}'")
    if number_of_files_that_could_not_be_processed > 0:
        print(f"Warning: Could not process {number_of_files_that_could_not_be_processed} files in the dist folder. Please check the error messages above for more details.")
    else:
        print("All files in the dist folder were processed successfully.")


if __name__ == "__main__":
    main()