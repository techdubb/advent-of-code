class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

    def setPrev(self, new_prev):
        self.prev = new_prev

    def insert(self, node):
        next = self.getNext()
        self.setNext(node)
        node.setPrev(self)
        node.setNext(next)
        next.setPrev(node)

    def removeNext(self):
        next = self.getNext()
        self.setNext(next.getNext())
        self.getNext().setPrev(self)

        return next


###########################################################

def parse_input(input):
    split_input = input.split(' ')
    return split_input[0], split_input[6]

def get_current_player(current_player, total_players):
    player = current_player % int(total_players)
    if player == 0:
        return total_players
    else:
        return player

# input = '13 players; last marble is worth 7999 points'
# input = '10 players; last marble is worth 1618 points'
# input = '471 players; last marble is worth 72026 points'
# input = '9 players; last marble is worth 25 points'
input = '471 players; last marble is worth 7202600 points'

total_players, total_marbles = parse_input(input)

current_marble = 0
current_player = 0

current_node = Node(0)
scores = dict()

# print the_circle
while current_marble < int(total_marbles):
    # print current_marble
    current_marble += 1
    current_player += 1
    player = get_current_player(current_player, total_players)

    if (current_marble % 23) == 0:
        for i in range(8):
            current_node = current_node.getPrev()

        popped_marble = current_node.removeNext()
        current_node = current_node.getNext()
        scores[player] = scores.get(player, 0) + current_marble + popped_marble.getData()
    else:
        current_node = current_node.getNext()

        node = Node(current_marble)

        current_node.insert(node)
        current_node = node

print "*****"

print 'High Score!'
print max(scores.values())