from ui import *

repo = Repository("players.txt")
service = Service(repo)
ui = UI(service)
ui.start()