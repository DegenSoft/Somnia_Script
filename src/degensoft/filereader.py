from loguru import logger
from .decryption import is_base64, decrypt_private_key
from .utils import load_lines


def load_and_decrypt_wallets(file_name,filename, password=''):
    """
    Will load wallets.txt file, if wallets was encrypted, trying to decrypt with the password provided
    :param filename:
    :param password:
    :param shuffle:
    :return:
    """
    lines = load_lines(filename)
    wallets = []
    for line in lines:
        if password and is_base64(line):
            wallets.append(decrypt_private_key(line, password))
        else:
            wallets.append(line)
    logger.success(f"Successfully loaded {len(wallets)} {file_name}.")
    return wallets