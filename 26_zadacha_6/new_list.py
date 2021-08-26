class ListElement:

    def __init__(self, index, data, link):
        self.index = index
        self.data = data
        self.link = link


class NewList:

    def __init__(self, *data_list):
        self.last_id = None
        self.index = len(data_list) - 1
        for data in data_list[::-1]:
            new_element = ListElement(index=self.index, data=data, link=self.last_id)
            self.index -= 1
            self.last_id = new_element
        self.__start_list_address_temp = self.last_id
        self.__start_const = self.__start_list_address_temp

    def __iter__(self):
        self.__start_list_address_temp = self.__start_const
        return self

    def __next__(self):
        try:
            element_to_show = self.__start_list_address_temp
            self.__start_list_address_temp = self.__start_list_address_temp.link
            return element_to_show.data
        except AttributeError:
            raise StopIteration

    def append(self, data):
        self.__start_list_address_temp = self.__start_const
        while self.__start_list_address_temp.link != None:
            self.__start_list_address_temp = self.__start_list_address_temp.link
        new_index = self.__start_list_address_temp.index + 1
        self.__start_list_address_temp.link = ListElement(index=new_index, data=data, link=None)

    def index_changer(self, link):
        current_elem = link
        while current_elem.link != None:
            current_elem.index -= 1
            current_elem = current_elem.link

    def remove(self, data):
        current_elem = self.__start_const
        previous_elem = self.__start_const
        while current_elem.link != None:
            x = current_elem.data
            if current_elem.data != data:
                previous_elem = current_elem
                current_elem = current_elem.link
            else:
                if current_elem == previous_elem:
                    self.__start_const = current_elem.link
                    self.index_changer(current_elem.link)
                    break
                else:
                    previous_elem.link = current_elem.link
                    self.index_changer(current_elem.link)
                    break
        else:
            if current_elem.data != data:
                raise ValueError('Такого элемента нет в списке')
            else:
                previous_elem.link = None

    def get(self, index: int) -> int:
        current_elem = self.__start_const
        while current_elem.link != None:
            if current_elem.index != index:
                current_elem = current_elem.link
            else:
                return current_elem.data
        else:
            raise IndexError('Нет элемента с таким индексом')
