import argparse
from pathlib import Path
from json import dump, load
from shutil import copytree
from lib.combining_folders import combiningFolders

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Build the cokurs website.")
    
    # Add the --export-folder argument
    parser.add_argument(
        '-e', '--export-folder',
        type=str,
            help='Path to the export folder where the website data that is exported from the dist folder of the cokurs website will be stored. The format of this folder is the same as the folder that is used when running the build_website.py script with the --import-folder argument. If there is no content in the dist folder a default export folder will be created.',
            required=False
        )
    parser.add_argument(
        '-d', '--dist-folder',
        type=str,
        help='Path to the dist folder of the cokurs website. If this argument is not provided, the script will look for a dist folder in the same directory as the script.',
        required=False
    )
    parser.add_argument(
        '-m', '--metadata-folder',
        type=str,
        help='Path to the metadata folder of the cokurs website. If this argument is not provided, the script will look for a metadata folder in the same directory as the script.',
        required=False
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Access the --export-folder argument
    if not args.export_folder:
        print("No export folder provided. This argument is required to export the data of the website. Please provide an export folder using the --export-folder argument.")
        return
    export_path = Path(args.export_folder)
    if export_path.exists():
        print(f"Error: The provided export folder path '{export_path}' already exists. Please provide a non-existing folder path to avoid overwriting existing data.")
        return
    
    # Get the dist folder path
    if args.dist_folder:
        print(f"Dist folder provided: {args.dist_folder}")
        dist_path = Path(args.dist_folder)
        if not dist_path.is_dir():
            print(f"Error: The provided dist folder path '{dist_path}' is not a directory.")
            return
    else:
        print("No dist folder provided. Looking for a dist folder in the same directory as the script.")
        dist_path = Path(__file__).parent / "dist"
        if not dist_path.is_dir():
            print(f"Error: No dist folder found in the same directory as the script. Please provide a dist folder using the --dist-folder argument.")
            return

    # Get the metadata folder path
    if args.metadata_folder:
        print(f"Metadata folder provided: {args.metadata_folder}")
        metadata_path = Path(args.metadata_folder)
        if not metadata_path.is_dir():
            print(f"Error: The provided metadata folder path '{metadata_path}' is not a directory.")
            return
    else:
        print("No metadata folder provided. Looking for a metadata folder in the same directory as the script.")
        metadata_path = Path(__file__).parent / "metadata"
        if not metadata_path.is_dir():
            print(f"Error: No metadata folder found in the same directory as the script.")
            return
        
    # Create the export folder
    try:
        export_path.mkdir(parents=True, exist_ok=False)
        print(f"Created export folder at: {export_path}")
    except Exception as e:
        print(f"Error: Could not create export folder at '{export_path}'. {e}")
        return
    
    # Copy the content of the metadata folder to the export folder
    print(f"Copying content from metadata folder to export folder...")
    copied_files_count = 0
    copied_directories_count = 0
    for item in metadata_path.iterdir():
        dest = export_path / item.name
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
    
    # Copy the combining folders to the export folder
    print("Copy the combining folders to the export folder")
    for dirName in combiningFolders:
        fromPath = dist_path / dirName
        if fromPath.isDir():
            copytree(fromPath, export_path / dirName)

if __name__ == "__main__":
    main()