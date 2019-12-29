def readFromFile(path, mode):
    try:
        with open(path, mode) as file_handler:
            for line in file_handler:
                yield line
    except IOError:
        print(f"Ошибка при чтении с файла {path}")

def writeToFile(path, mode, array):
    try:
        with open(path, mode) as file_handler:
            for line in array:
                file_handler.write(line)
    except IOError:
        print(f"Ошибка при записи в файл {path}")

def SignAuthor(pathsToFile, pathToSign):
    sign = list(readFromFile(pathToSign, 'r'))
    sign = sign[::-1]

    for path in pathsToFile:
        readedData = list(readFromFile(path, 'r'))
        for line in sign:
            readedData.insert(0, line)
        writeToFile(path, 'w', readedData)

if __name__ == '__main__':
    SignAuthor(['code.txt'], 'sign.txt')