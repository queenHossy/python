x = input('file name:').strip().lower()   # Prompt the user for a file name, remove extra whitespace, and convert to lowercase

if x.endswith('.gif'):    # Check if the file name ends with '.gif'
    print('image/gif' , end="")    # Print the corresponding media type for GIF images
elif x.endswith('.jpg') or x.endswith('.jpeg'):  # Check if the file name ends with '.jpg' or '.jpeg'
    print('image/jpeg' , end="")    # Print the corresponding media type for JPG images
elif x.endswith('.png'):  # Check if the file name ends with the extension '.png'
    print('image/png' , end="")    # Print the corresponding media type for PNG images
elif x.endswith('.pdf'):  # Check if the file name ends with the extension '.pdf'
    print('application/pdf' , end="")    # Print the corresponding media type for PDF documents
elif x.endswith('.txt'):  # Check if the file name ends with the extension '.txt'
    print('text/plain' , end="")    # Print the corresponding media type for plain text files
elif x.endswith('zip'):   # Check if the file name ends with the extension '.zip'
    print('application/zip' , end="")    # Print the corresponding media type for ZIP archives
else:         # Default case if extension does not match any supported type
    print('application/octet-stream' , end="")    # Print media type for fallback/unrecognized file types

# Purpose:
# This code prompts the user for a filename string
#  and determines its media/MIME type by checking its extension using Python's
