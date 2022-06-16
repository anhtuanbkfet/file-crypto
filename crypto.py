import pyAesCrypt
import argparse
from os import stat, remove


bufferSize = 64 * 1024
password = "tuan.na3"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a encode/decode crypto file')
    parser.add_argument('--mode', required=True, default= 'encript')
    parser.add_argument('--input', required=True, help='path to input file')
    parser.add_argument('--output', required=True, help='path to output file')

    args = parser.parse_args()

    in_file_path = args.input
    out_file_path = args.output

    if args.mode == 'encript':
        # encrypt
        with open(in_file_path, "rb") as fIn:
            with open(out_file_path, "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
    else:

        # get encrypted file size
        encFileSize = stat(in_file_path).st_size

        # decrypt
        with open(in_file_path, "rb") as fIn:
            try:
                with open(out_file_path, "wb") as fOut:
                    # decrypt file stream
                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
            except ValueError:
                # remove output file on error
                remove(out_file_path)
