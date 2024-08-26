"""
    Folder_Hider

    Суть проги - прятать папку. Просто заполните поля ниже - и всё. Зачем это сделано? Попросил один друг, а ещё мой гитхаб пустует...

    Версия: 1.2.6 r
    Разработчик: Urban Egor
    Разработано в России
"""


import os
import shutil
import zipfile

from cryptography.fernet import Fernet


def archive_folder(folder_path: str, archive_name: str) -> None:
    """

    :param folder_path:
    :param archive_name:
    :return: None

    Архивирование папки
    """
    shutil.make_archive(archive_name, 'zip', folder_path)
    shutil.rmtree(folder_path)


def extract_archive(archive_path: str, extract_to: str) -> None:
    """

    :param archive_path:
    :param extract_to:
    :return: None

    Распаковывает папку

    """
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def encrypt_file(file_path: str, key: bytes) -> None:
    """

    :param file_path:
    :param key:
    :return: None

    Шифрует архив

    """
    with open(file_path, 'rb') as file:
        file_data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(file_path: str, key: bytes) -> None:
    """

    :param file_path:
    :param key:
    :return: None

    Расшифровывает архив

    """
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)



def main():
    folder_name = 'Имя папки, что нужно зашифровать'
    archive_name = 'temp' # Имя временного архива, хотя вы всё равно его не увидете
    file_name = 'Имя файла, которым назовётся зашифрованный файл'
    key = b'32-байт ключ, в base64'

    if os.path.exists(file_name):
        decrypt_file(file_name, key)
        extract_archive(file_name, folder_name)
        os.remove(file_name)
    else:
        if os.path.exists(folder_name):
            pass
        else:
            while os.path.exists(folder_name) == False:
                folder_name = input("Если папка будет не найдена - тут сообщение, которое спросит имя папки: ")

        archive_folder(folder_name, archive_name)
        encrypt_file(archive_name + '.zip', key)
        os.rename(archive_name + '.zip', file_name)

if __name__ == "__main__":
    main()
