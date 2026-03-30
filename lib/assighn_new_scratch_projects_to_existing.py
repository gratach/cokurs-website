import hashlib
import os
import re


def _hash_file(path, chunk_size=1024 * 1024):
    """
    Compute SHA256 hash of a file efficiently using chunks.
    """
    sha = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha.update(chunk)

    return sha.hexdigest()


def _is_positive_int_filename(name):
    """
    Check if filename is a positive integer without extension.
    """
    return re.fullmatch(r"[1-9][0-9]*", name) is not None


def assignNewFilesToExistingOnes(existing_dir_path, new_dir_path):
    """
    Assign new files to existing ones based on identical byte content.

    Args:
        existing_dir_path: pathlib.Path of directory with existing files
        new_dir_path: pathlib.Path of directory with new files

    Returns:
        assignment_dict: dict mapping new filenames to target filenames
    """

    assignment_dict = {}

    # --------------------------------
    # Step 1: Collect existing files and their hashes
    # --------------------------------

    existing_hash_to_names = {}
    used_names = set()

    for file_path in existing_dir_path.iterdir():
        if not file_path.is_file():
            continue

        name = file_path.name
        used_names.add(name)

        file_hash = _hash_file(file_path)

        if file_hash not in existing_hash_to_names:
            existing_hash_to_names[file_hash] = []

        existing_hash_to_names[file_hash].append(name)

    # --------------------------------
    # Step 2: Process new files
    # --------------------------------

    unmatched_files = {}

    for file_path in new_dir_path.iterdir():
        if not file_path.is_file():
            continue

        name = file_path.name
        file_hash = _hash_file(file_path)

        # If identical content exists
        if file_hash in existing_hash_to_names:
            target_name = existing_hash_to_names[file_hash][0]
            assignment_dict[name] = target_name
        else:
            unmatched_files[name] = file_hash

    # --------------------------------
    # Step 3: Sort unmatched files
    # --------------------------------

    numeric_files = []
    other_files = []

    for name in unmatched_files.keys():
        base, ext = os.path.splitext(name)

        if ext == "" and _is_positive_int_filename(base):
            numeric_files.append(name)
        else:
            other_files.append(name)

    # Sort numeric files by integer value
    numeric_files.sort(key=lambda x: int(x))

    # Sort other files alphabetically
    other_files.sort()

    ordered_unmatched = numeric_files + other_files

    # --------------------------------
    # Step 4: Find unused positive integers
    # --------------------------------

    used_numbers = set()

    for name in used_names:
        base, ext = os.path.splitext(name)

        if ext == "" and _is_positive_int_filename(base):
            used_numbers.add(int(base))

    def next_free_number():
        """
        Generator for free positive integers.
        """
        i = 1
        while True:
            if i not in used_numbers:
                yield i
            i += 1

    free_numbers = next_free_number()

    # --------------------------------
    # Step 5: Assign new names
    # --------------------------------

    for name in ordered_unmatched:
        file_hash = unmatched_files[name]
        if file_hash in existing_hash_to_names:
            target_name = existing_hash_to_names[file_hash][0]
            assignment_dict[name] = target_name
            continue

        num = next(free_numbers)
        used_numbers.add(num)

        target_name = str(num)

        assignment_dict[name] = target_name
        
        existing_hash_to_names[file_hash] = [target_name]

    # --------------------------------
    # Step 6: Create missing files in existing directory
    # --------------------------------

    for new_name, target_name in assignment_dict.items():

        source_path = new_dir_path / new_name
        target_path = existing_dir_path / target_name

        # Only create file if it does not already exist
        if not target_path.exists():

            # Copy file content in binary mode
            with open(source_path, "rb") as src, open(target_path, "wb") as dst:
                while True:
                    chunk = src.read(1024 * 1024)  # Read in 1 MB blocks
                    if not chunk:
                        break
                    dst.write(chunk)

    return assignment_dict