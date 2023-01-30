import os.path

from constants.text_of_this import THIS_TEXT


class FileModification:
    def __init__(self):
        self.file_name = 'this_text.txt'

    def create_txt_file(self, file_data: str = THIS_TEXT):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(file_data)

    def __load_data_from_file(self):
        with open(self.file_name, 'r') as file:
            file_data = file.read()
        return file_data.split()

    def find_words(self, letters: str):
        data = self.__load_data_from_file()
        word_list = []
        for word in data:
            for letter in letters:
                if letter not in word.lower():
                    break
            else:
                word_list.append(word.strip('.,!*:'))
        print(word_list)

        return word_list

    def append_word(self, words: str):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(f'\n{words}')

    def delete_data_from_file(self):
        with open(self.file_name, 'r+') as file:
            file.truncate(0)

    def find_words_with_letters_and_length_of_word(self, letter: str, length: int):
        words = self.__load_data_from_file()
        result = []
        for word in words:
            if length is None:
                if letter in word:
                    result.append(word)
            else:
                if letter in word and len(word) == length:
                    result.append(word)

        return result

    def delete_file(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        else:
            print(f'File {self.file_name} does not exist')


buttons = FileModification()
buttons.create_txt_file()
