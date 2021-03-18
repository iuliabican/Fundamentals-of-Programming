from domain import Player


class RepositoryError(Exception):
    pass


class Repository:
    def __init__(self, fileName):
        self._fileName = fileName
        self._data = []
        self._loadFile()

    def getAll(self):
        return self._data

    """
    def _saveFile(self):
	# ! .strip() for strings when saving
        try:
            f = open(self._fileName, "w")
            lst = self.getAll()
            for x in lst:
                line = str(x.ID) + ", "
                for i in x.Persons:
                    line += str(i) + ", "
                for i in x.Date:
                    line += str(i) + ", "
                for i in x.Time:
                    line += str(i) + ", "
                line += x.Description
                f.write(line + "\n")
            f.close()
        except IOError:
            raise RepositoryError("Error saving file")
    """

    def _loadFile(self):
        try:
            f = open(self._fileName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                for i in attrs:
                    i.strip()
                params = [0, "", 0]
                params[0] = int(attrs[0])  # id
                params[1] = attrs[1]  # name
                params[2] = int(attrs[2])  # strength
                p = Player(params[0], params[1], params[2])
                self._data.append(p)
                line = f.readline().strip()
            f.close()
        except IOError:
            raise RepositoryError("Error loading file")
