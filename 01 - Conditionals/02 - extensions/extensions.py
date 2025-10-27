extension = input("File name: ")
if ".gif" in extension:
    print("image/gif")
elif ".jpg" in extension:
    print("image/jpg")
elif ".jpeg" in extension:
    print("image/jpeg")
elif ".png" in extension:
    print("image/png")
elif ".pdf" in extension:
    print("application/pdf")
elif ".txt" in extension:
    print("txt/plain")
elif ".zip" in extension:
    print("application/zip")