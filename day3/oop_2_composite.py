class BaseNode:
    name = "<Unknown>"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass


class File(BaseNode):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f'file: "{self.name}"'


class Dir(BaseNode):
    def __init__(self, name):
        super().__init__(name)
        self._nodes = []

    def add(self, node):
        self._nodes.append(node)

    def remove(self, node):
        self._nodes.remove(node)

    def __repr__(self):
        result = [f'directory: {self.name}']

        if len(self._nodes):
            result.append(" (")
            for i in self._nodes:
                result.append(f"{i}")
                if i != self._nodes[-1]:
                    result.append(", ")
            result.append(")")
        else:
            result.append(" (empty)")

        return "".join(result)


d1 = Dir('dir1') # папка на верхнем уровне
d1.add(File('text1.txt'))
d2 = Dir('dir2')
d1.add(d2)
d3 = Dir('dir3')
d1.add(d3)
d1.remove(d3) # пример удаления вложенной структуры
d4 = Dir('dir4')
d2.add(d4)
d4.add(File('image1.txt'))
d4.add(File('text2.txt'))
d1.add(File('paper1.pdf'))
d2.add(Dir('dir5'))

print(d1)
