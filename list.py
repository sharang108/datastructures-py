class List:

    def __init__(self):
        self.start = None
        self.current = None

    def add_element(self, value):
        node = {'value': value, 'next': None}
        if not self.start:
            self.start = node
            self.current = node
        else:
            self.current['next'] = node
            self.current = node

    def traverse_list(self):
        node = self.start
        str_list = ''
        while True:
            str_list += str(node['value'])+str('->')
            node = node['next']
            if node is None:
                str_list += "END"
                break
        print(str_list)

    def delete_element(self, del_key):
        if self.current['value'] == del_key:
            self.current = self.current['next']

        elif self.start['value'] == del_key:
            self.start = self.start['next']

        else:
            pointer = self.start
            prev = None
            while True:
                if pointer['value'] == del_key:
                    prev['next'] = pointer['next']
                    print(str(pointer['value'])+" is deleted")
                    break
                if pointer['next'] is None:
                    print('No such element exists')
                    break
                prev = pointer
                pointer = pointer['next']
