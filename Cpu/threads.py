import os

def split_images_into_lists(directory_path, num_lists):
    # Get a list of image files in the directory
    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    # Calculate the number of images per list
    images_per_list = len(image_files) // num_lists
    # Starting index for the subset of images
    start_idx = 0
    # List to hold the lists of image files
    image_lists = []

    # Create the lists of image files
    for i in range(num_lists):
        # Calculate the end index for the subset of images
        end_idx = start_idx + images_per_list if i < num_lists - 1 else len(image_files)
        # Get the subset of image files
        sublist = image_files[start_idx:end_idx]
        # Append the sublist to the image_lists
        image_lists.append(sublist)
        # Update the start index for the next sublist
        start_idx = end_idx

    return image_lists

# Example usage:
directory_path = "out"
num_lists = int(input("Enter the number of lists: "))
lists_of_images = split_images_into_lists(directory_path, num_lists)
for i, image_list in enumerate(lists_of_images):
    print(f"List {i+1}: {image_list}")
