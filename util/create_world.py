from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

# Create a room object for every index in the array
dungeon_objects = [[Room(title="9,0", description="dungeon"), Room(title="9,1", description="dungeon"), Room(title="9,2", description="dungeon"),Room(title="9,3", description="dungeon"), Room(title="9,4", description="dungeon"), Room(title="9,5", description="dungeon"),Room(title="9,6", description="dungeon"), Room(title="9,7", description="dungeon"), Room(title="9,8", description="dungeon"),Room(title="9,9", description="dungeon")],[Room(title="8,0", description="dungeon"), Room(title="8,1", description="dungeon"), Room(title="8,2", description="dungeon"),Room(title="8,3", description="dungeon"), Room(title="8,4", description="dungeon"), Room(title="8,5", description="dungeon"),Room(title="8,6", description="dungeon"), Room(title="8,7", description="dungeon"), Room(title="8,8", description="dungeon"),Room(title="8,9", description="dungeon")],[Room(title="7,0", description="dungeon"), Room(title="7,1", description="dungeon"), Room(title="7,2", description="dungeon"),Room(title="7,3", description="dungeon"), Room(title="7,4", description="dungeon"), Room(title="7,5", description="dungeon"),Room(title="7,6", description="dungeon"), Room(title="7,7", description="dungeon"), Room(title="7,8", description="dungeon"),Room(title="7,9", description="dungeon")],[Room(title="6,0", description="dungeon"), Room(title="6,1", description="dungeon"), Room(title="6,2", description="dungeon"),Room(title="6,3", description="dungeon"), Room(title="6,4", description="dungeon"), Room(title="6,5", description="dungeon"),Room(title="6,6", description="dungeon"), Room(title="6,7", description="dungeon"), Room(title="6,8", description="dungeon"),Room(title="6,9", description="dungeon")],[Room(title="5,0", description="dungeon"), Room(title="5,1", description="dungeon"), Room(title="5,2", description="dungeon"),Room(title="5,3", description="dungeon"), Room(title="5,4", description="dungeon"), Room(title="5,5", description="dungeon"),Room(title="5,6", description="dungeon"), Room(title="5,7", description="dungeon"), Room(title="5,8", description="dungeon"),Room(title="5,9", description="dungeon")],[Room(title="4,0", description="dungeon"), Room(title="4,1", description="dungeon"), Room(title="4,2", description="dungeon"),Room(title="4,3", description="dungeon"), Room(title="4,4", description="dungeon"), Room(title="4,5", description="dungeon"),Room(title="4,6", description="dungeon"), Room(title="4,7", description="dungeon"), Room(title="4,8", description="dungeon"),Room(title="4,9", description="dungeon")],[Room(title="3,0", description="dungeon"), Room(title="3,1", description="dungeon"), Room(title="3,2", description="dungeon"),Room(title="3,3", description="dungeon"), Room(title="3,4", description="dungeon"), Room(title="3,5", description="dungeon"),Room(title="3,6", description="dungeon"), Room(title="3,7", description="dungeon"), Room(title="3,8", description="dungeon"),Room(title="3,9", description="dungeon")],[Room(title="2,0", description="dungeon"), Room(title="2,1", description="dungeon"), Room(title="2,2", description="dungeon"),Room(title="2,3", description="dungeon"), Room(title="2,4", description="dungeon"), Room(title="2,5", description="dungeon"),Room(title="2,6", description="dungeon"), Room(title="2,7", description="dungeon"), Room(title="2,8", description="dungeon"),Room(title="2,9", description="dungeon")],[Room(title="1,0", description="dungeon"), Room(title="1,1", description="dungeon"), Room(title="1,2", description="dungeon"),Room(title="1,3", description="dungeon"), Room(title="1,4", description="dungeon"), Room(title="1,5", description="dungeon"),Room(title="1,6", description="dungeon"), Room(title="1,7", description="dungeon"), Room(title="1,8", description="dungeon"),Room(title="1,9", description="dungeon")],[Room(title="0,0", description="dungeon"), Room(title="0,1", description="dungeon"), Room(title="0,2", description="dungeon"),Room(title="0,3", description="dungeon"), Room(title="0,4", description="dungeon"), Room(title="0,5", description="dungeon"),Room(title="0,6", description="dungeon"), Room(title="0,7", description="dungeon"), Room(title="0,8", description="dungeon"),Room(title="0,9", description="dungeon")]]

forest_objects = [[Room(title="9,0", description="field"), Room(title="9,1", description="field"), Room(title="9,2", description="field"),Room(title="9,3", description="field"), Room(title="9,4", description="field"), Room(title="9,5", description="field"),Room(title="9,6", description="field"), Room(title="9,7", description="field"), Room(title="9,8", description="field"),Room(title="9,9", description="field")],[Room(title="8,0", description="field"), Room(title="8,1", description="field"), Room(title="8,2", description="field"),Room(title="8,3", description="field"), Room(title="8,4", description="field"), Room(title="8,5", description="field"),Room(title="8,6", description="field"), Room(title="8,7", description="field"), Room(title="8,8", description="field"),Room(title="8,9", description="field")],[Room(title="7,0", description="field"), Room(title="7,1", description="field"), Room(title="7,2", description="field"),Room(title="7,3", description="field"), Room(title="7,4", description="field"), Room(title="7,5", description="field"),Room(title="7,6", description="field"), Room(title="7,7", description="field"), Room(title="7,8", description="field"),Room(title="7,9", description="field")],[Room(title="6,0", description="field"), Room(title="6,1", description="field"), Room(title="6,2", description="field"),Room(title="6,3", description="field"), Room(title="6,4", description="field"), Room(title="6,5", description="field"),Room(title="6,6", description="field"), Room(title="6,7", description="field"), Room(title="6,8", description="field"),Room(title="6,9", description="field")],[Room(title="5,0", description="field"), Room(title="5,1", description="field"), Room(title="5,2", description="field"),Room(title="5,3", description="field"), Room(title="5,4", description="field"), Room(title="5,5", description="field"),Room(title="5,6", description="field"), Room(title="5,7", description="field"), Room(title="5,8", description="field"),Room(title="5,9", description="field")],[Room(title="4,0", description="field"), Room(title="4,1", description="field"), Room(title="4,2", description="field"),Room(title="4,3", description="field"), Room(title="4,4", description="field"), Room(title="4,5", description="field"),Room(title="4,6", description="field"), Room(title="4,7", description="field"), Room(title="4,8", description="field"),Room(title="4,9", description="field")],[Room(title="3,0", description="field"), Room(title="3,1", description="field"), Room(title="3,2", description="field"),Room(title="3,3", description="field"), Room(title="3,4", description="field"), Room(title="3,5", description="field"),Room(title="3,6", description="field"), Room(title="3,7", description="field"), Room(title="3,8", description="field"),Room(title="3,9", description="field")],[Room(title="2,0", description="field"), Room(title="2,1", description="field"), Room(title="2,2", description="field"),Room(title="2,3", description="field"), Room(title="2,4", description="field"), Room(title="2,5", description="field"),Room(title="2,6", description="field"), Room(title="2,7", description="field"), Room(title="2,8", description="field"),Room(title="2,9", description="field")],[Room(title="1,0", description="field"), Room(title="1,1", description="field"), Room(title="1,2", description="field"),Room(title="1,3", description="field"), Room(title="1,4", description="field"), Room(title="1,5", description="field"),Room(title="1,6", description="field"), Room(title="1,7", description="field"), Room(title="1,8", description="field"),Room(title="1,9", description="field")],[Room(title="0,0", description="field"), Room(title="0,1", description="field"), Room(title="0,2", description="field"),Room(title="0,3", description="field"), Room(title="0,4", description="field"), Room(title="0,5", description="field"),Room(title="0,6", description="field"), Room(title="0,7", description="field"), Room(title="0,8", description="field"),Room(title="0,9", description="field")]]

ryan_room_objects = [[Room(title="9,0", description="house"), Room(title="9,1", description="house"), Room(title="9,2", description="house"),Room(title="9,3", description="house"), Room(title="9,4", description="house"), Room(title="9,5", description="house"),Room(title="9,6", description="house"), Room(title="9,7", description="house"), Room(title="9,8", description="house"),Room(title="9,9", description="house")],[Room(title="8,0", description="house"), Room(title="8,1", description="house"), Room(title="8,2", description="house"),Room(title="8,3", description="house"), Room(title="8,4", description="house"), Room(title="8,5", description="house"),Room(title="8,6", description="house"), Room(title="8,7", description="house"), Room(title="8,8", description="house"),Room(title="8,9", description="house")],[Room(title="7,0", description="house"), Room(title="7,1", description="house"), Room(title="7,2", description="house"),Room(title="7,3", description="house"), Room(title="7,4", description="house"), Room(title="7,5", description="house"),Room(title="7,6", description="house"), Room(title="7,7", description="house"), Room(title="7,8", description="house"),Room(title="7,9", description="house")],[Room(title="6,0", description="house"), Room(title="6,1", description="house"), Room(title="6,2", description="house"),Room(title="6,3", description="house"), Room(title="6,4", description="house"), Room(title="6,5", description="house"),Room(title="6,6", description="house"), Room(title="6,7", description="house"), Room(title="6,8", description="house"),Room(title="6,9", description="house")],[Room(title="5,0", description="house"), Room(title="5,1", description="house"), Room(title="5,2", description="house"),Room(title="5,3", description="house"), Room(title="5,4", description="house"), Room(title="5,5", description="house"),Room(title="5,6", description="house"), Room(title="5,7", description="house"), Room(title="5,8", description="house"),Room(title="5,9", description="house")],[Room(title="4,0", description="house"), Room(title="4,1", description="house"), Room(title="4,2", description="house"),Room(title="4,3", description="house"), Room(title="4,4", description="house"), Room(title="4,5", description="house"),Room(title="4,6", description="house"), Room(title="4,7", description="house"), Room(title="4,8", description="house"),Room(title="4,9", description="house")],[Room(title="3,0", description="house"), Room(title="3,1", description="house"), Room(title="3,2", description="house"),Room(title="3,3", description="house"), Room(title="3,4", description="house"), Room(title="3,5", description="house"),Room(title="3,6", description="house"), Room(title="3,7", description="house"), Room(title="3,8", description="house"),Room(title="3,9", description="house")],[Room(title="2,0", description="house"), Room(title="2,1", description="house"), Room(title="2,2", description="house"),Room(title="2,3", description="house"), Room(title="2,4", description="house"), Room(title="2,5", description="house"),Room(title="2,6", description="house"), Room(title="2,7", description="house"), Room(title="2,8", description="house"),Room(title="2,9", description="house")],[Room(title="1,0", description="house"), Room(title="1,1", description="house"), Room(title="1,2", description="house"),Room(title="1,3", description="house"), Room(title="1,4", description="house"), Room(title="1,5", description="house"),Room(title="1,6", description="house"), Room(title="1,7", description="house"), Room(title="1,8", description="house"),Room(title="1,9", description="house")],[Room(title="0,0", description="house"), Room(title="0,1", description="house"), Room(title="0,2", description="house"),Room(title="0,3", description="house"), Room(title="0,4", description="house"), Room(title="0,5", description="house"),Room(title="0,6", description="house"), Room(title="0,7", description="house"), Room(title="0,8", description="house"),Room(title="0,9", description="house")]]

boss_room_objects = [[Room(title="9,0", description="basement"), Room(title="9,1", description="basement"), Room(title="9,2", description="basement"),Room(title="9,3", description="basement"), Room(title="9,4", description="basement"), Room(title="9,5", description="basement"),Room(title="9,6", description="basement"), Room(title="9,7", description="basement"), Room(title="9,8", description="basement"),Room(title="9,9", description="basement")],[Room(title="8,0", description="basement"), Room(title="8,1", description="basement"), Room(title="8,2", description="basement"),Room(title="8,3", description="basement"), Room(title="8,4", description="basement"), Room(title="8,5", description="basement"),Room(title="8,6", description="basement"), Room(title="8,7", description="basement"), Room(title="8,8", description="basement"),Room(title="8,9", description="basement")],[Room(title="7,0", description="basement"), Room(title="7,1", description="basement"), Room(title="7,2", description="basement"),Room(title="7,3", description="basement"), Room(title="7,4", description="basement"), Room(title="7,5", description="basement"),Room(title="7,6", description="basement"), Room(title="7,7", description="basement"), Room(title="7,8", description="basement"),Room(title="7,9", description="basement")],[Room(title="6,0", description="basement"), Room(title="6,1", description="basement"), Room(title="6,2", description="basement"),Room(title="6,3", description="basement"), Room(title="6,4", description="basement"), Room(title="6,5", description="basement"),Room(title="6,6", description="basement"), Room(title="6,7", description="basement"), Room(title="6,8", description="basement"),Room(title="6,9", description="basement")],[Room(title="5,0", description="basement"), Room(title="5,1", description="basement"), Room(title="5,2", description="basement"),Room(title="5,3", description="basement"), Room(title="5,4", description="basement"), Room(title="5,5", description="basement"),Room(title="5,6", description="basement"), Room(title="5,7", description="basement"), Room(title="5,8", description="basement"),Room(title="5,9", description="basement")],[Room(title="4,0", description="basement"), Room(title="4,1", description="basement"), Room(title="4,2", description="basement"),Room(title="4,3", description="basement"), Room(title="4,4", description="basement"), Room(title="4,5", description="basement"),Room(title="4,6", description="basement"), Room(title="4,7", description="basement"), Room(title="4,8", description="basement"),Room(title="4,9", description="basement")],[Room(title="3,0", description="basement"), Room(title="3,1", description="basement"), Room(title="3,2", description="basement"),Room(title="3,3", description="basement"), Room(title="3,4", description="basement"), Room(title="3,5", description="basement"),Room(title="3,6", description="basement"), Room(title="3,7", description="basement"), Room(title="3,8", description="basement"),Room(title="3,9", description="basement")],[Room(title="2,0", description="basement"), Room(title="2,1", description="basement"), Room(title="2,2", description="basement"),Room(title="2,3", description="basement"), Room(title="2,4", description="basement"), Room(title="2,5", description="basement"),Room(title="2,6", description="basement"), Room(title="2,7", description="basement"), Room(title="2,8", description="basement"),Room(title="2,9", description="basement")],[Room(title="1,0", description="basement"), Room(title="1,1", description="basement"), Room(title="1,2", description="basement"),Room(title="1,3", description="basement"), Room(title="1,4", description="basement"), Room(title="1,5", description="basement"),Room(title="1,6", description="basement"), Room(title="1,7", description="basement"), Room(title="1,8", description="basement"),Room(title="1,9", description="basement")],[Room(title="0,0", description="basement"), Room(title="0,1", description="basement"), Room(title="0,2", description="basement"),Room(title="0,3", description="basement"), Room(title="0,4", description="basement"), Room(title="0,5", description="basement"),Room(title="0,6", description="basement"), Room(title="0,7", description="basement"), Room(title="0,8", description="basement"),Room(title="0,9", description="basement")]]


forest_movements=[[15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [8,13,13,13,9,15,15,15,15,15],[10,14,14,14,11,15,2,15,15,15],[16,14,14,14,14,13,11,15,15,15],[10,14,14,12,14,14,14,13,13,9],[10,14,6,15,10,14,14,14,14,11],[10,11,15,15,7,12,14,14,12,6],[10,11,15,15,15,15,10,11,15,15],[7,12,12,6,15,15,7,12,16,15]]

dungeon_movements=[[15,15,15,15,15,15,15,15,15,15],[15,15,15,15,1,9,15,16,15,2],[15,15,15,15,15,4,8,14,13,11],[15,15,15,15,15,4,10,14,12,6],[15,2,15,8,13,14,14,11,15,15],[15,7,13,14,14,14,14,11,15,15],[15,15,7,14,14,14,14,14,13,9],[15,15,15,7,12,12,14,14,14,11],[15,2,15,15,15,15,10,11,16,4],[15,7,5,5,5,5,12,6,15,0]]

house_movements=[[15,15,15,15,15,15,15,15,15,15],[16,1,13,13,9,15,8,13,13,9],[15,15,10,14,11,15,10,12,12,6],[8,13,14,14,14,13,11,15,4,15],[16,14,14,14,14,14,11,15,4,15],[10,14,14,14,12,12,14,13,14,9],[10,14,14,6,15,15,7,14,14,11],[10,14,11,15,15,15,15,10,14,11],[10,14,14,9,15,15,8,14,14,11],[7,12,12,12,5,5,12,12,12,6]]

basement_movements=[[15,15,8,13,13,13,9,15,15,15],[15,15,10,14,12,12,12,13,9,15],[15,15,10,11,15,15,15,10,14,3],[8,13,14,11,15,2,15,10,14,11],[10,14,14,11,15,4,15,10,14,11],[10,14,14,11,15,4,15,10,14,11],[10,14,14,14,13,14,13,14,14,11],[7,12,14,14,14,14,14,14,14,6],[15,15,7,14,14,14,14,12,6,15],[15,15,15,16,16,16,16,15,15,15]]

def connectNorth(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1-1][index_2], "n")

def connectSouth(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1+1][index_2], "s")

def connectEast(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1][index_2+1], "e")

def connectWest(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1][index_2-1], "w")

  

# Save all rooms
for i in range(0,10):
  for j in range(0,10):
    dungeon_objects[i][j].save()
    forest_objects[i][j].save()
    ryan_room_objects[i][j].save()
    boss_room_objects[i][j].save()

def map_room(room_movement_array, room_object_array):
  for i in range(0,10):
    for j in range(0,10):
      if room_movement_array[i][j] == 0:
        connectNorth(i,j, room_object_array)
      elif room_movement_array[i][j] == 1:
        connectEast(i,j, room_object_array)
      elif room_movement_array[i][j] == 2:
        connectSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 3:
        connectWest(i,j, room_object_array)
      elif room_movement_array[i][j] == 4:
        connectNorth(i,j, room_object_array)
        connectSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 5:
        connectWest(i,j, room_object_array)
        connectEast(i,j, room_object_array)
      elif room_movement_array[i][j] == 6:
        connectNorth(i,j, room_object_array)
        connectWest(i,j, room_object_array)
      elif room_movement_array[i][j] == 7:
        connectNorth(i,j, room_object_array)
        connectEast(i,j, room_object_array)
      elif room_movement_array[i][j] == 8:
        connectEast(i,j, room_object_array)
        connectSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 9:
        connectWest(i,j, room_object_array)
        connectSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 10:
        connectNorth(i,j, room_object_array)
        connectEast(i,j, room_object_array)
        connectSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 11:
        connectNorth(i,j, room_object_array)
        connectWest(i,j, room_object_array)
        connectSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 12:
        connectWest(i,j, room_object_array)
        connectEast(i,j, room_object_array)
        connectNorth(i,j, room_object_array)
      elif room_movement_array[i][j] == 13:
        connectWest(i,j, room_object_array)
        connectEast(i,j, room_object_array)
        connectSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 14:
        connectNorth(i,j, room_object_array)
        connectEast(i,j, room_object_array)
        connectSouth(i,j, room_object_array)
        connectWest(i,j, room_object_array)
      elif room_movement_array[i][j] == 15: 
        pass

map_room(dungeon_movements, dungeon_objects)
map_room(forest_movements, forest_objects)
map_room(house_movements, ryan_room_objects)
map_room(basement_movements, boss_room_objects)

forest_objects[4][1].connectRooms(forest_objects[9][7], "w")

forest_objects[3][0].connectRooms(forest_objects[9][7], "s")

forest_objects[5][0].connectRooms(forest_objects[9][7], "n")

# forest_objects[9][7].connectRooms(forest_objects[4][1], "e")

forest_objects[9][7].connectRooms(dungeon_objects[7][8], "e")
dungeon_objects[7][8].connectRooms(forest_objects[9][7], "s")

dungeon_objects[2][7].connectRooms(ryan_room_objects[4][1], "n")
ryan_room_objects[4][1].connectRooms(dungeon_objects[2][7], "w")

ryan_room_objects[1][1].connectRooms(boss_room_objects[8][6], "w")

boss_room_objects[8][3].connectRooms(ryan_room_objects[1][1], "s")
boss_room_objects[8][4].connectRooms(ryan_room_objects[1][1], "s")
boss_room_objects[8][5].connectRooms(ryan_room_objects[1][1], "s")
boss_room_objects[8][6].connectRooms(ryan_room_objects[1][1], "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=forest_objects[9][0].id
  p.save()

