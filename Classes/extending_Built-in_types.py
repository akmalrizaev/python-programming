class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(List):
    def append(self, object):
        print("Append called")
        super().append(object)


text = Text("Python")
print(text.duplicate())

list = TrackableList()
list.append("1")