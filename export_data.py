import argparse
from pathlib import Path
from json import dump, load

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
    
    # Copy the config.json file from the metadata folder to the export folder
    try:
        with open(metadata_path / "config.json", "r") as f:
            config_data = load(f)
        with open(export_path / "config.json", "w") as f:
            dump(config_data, f, indent=4)
        print(f"Copied config.json from metadata folder to export folder.")
    except Exception as e:
        print(f"Error: Could not copy config.json from metadata folder to export folder. {e}")
        return

if __name__ == "__main__":
    main()