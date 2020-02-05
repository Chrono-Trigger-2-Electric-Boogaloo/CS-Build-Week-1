from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

# Create a room object for every index in the array
dungeon_objects = [[Room(title="9,0", description="dungeon"), Room(title="9,1", description="dungeon"), Room(title="9,2", description="dungeon"),Room(title="9,3", description="dungeon"), Room(title="9,4", description="dungeon"), Room(title="9,5", description="dungeon"),Room(title="9,6", description="dungeon"), Room(title="9,7", description="dungeon"), Room(title="9,8", description="dungeon"),Room(title="9,9", description="dungeon")],[Room(title="8,0", description="dungeon"), Room(title="8,1", description="dungeon"), Room(title="8,2", description="dungeon"),Room(title="8,3", description="dungeon"), Room(title="8,4", description="dungeon"), Room(title="8,5", description="dungeon"),Room(title="8,6", description="dungeon"), Room(title="8,7", description="dungeon"), Room(title="8,8", description="dungeon"),Room(title="8,9", description="dungeon")],[Room(title="7,0", description="dungeon"), Room(title="7,1", description="dungeon"), Room(title="7,2", description="dungeon"),Room(title="7,3", description="dungeon"), Room(title="7,4", description="dungeon"), Room(title="7,5", description="dungeon"),Room(title="7,6", description="dungeon"), Room(title="7,7", description="dungeon"), Room(title="7,8", description="dungeon"),Room(title="7,9", description="dungeon")],[Room(title="6,0", description="dungeon"), Room(title="6,1", description="dungeon"), Room(title="6,2", description="dungeon"),Room(title="6,3", description="dungeon"), Room(title="6,4", description="dungeon"), Room(title="6,5", description="dungeon"),Room(title="6,6", description="dungeon"), Room(title="6,7", description="dungeon"), Room(title="6,8", description="dungeon"),Room(title="6,9", description="dungeon")],[Room(title="5,0", description="dungeon"), Room(title="5,1", description="dungeon"), Room(title="5,2", description="dungeon"),Room(title="5,3", description="dungeon"), Room(title="5,4", description="dungeon"), Room(title="5,5", description="dungeon"),Room(title="5,6", description="dungeon"), Room(title="5,7", description="dungeon"), Room(title="5,8", description="dungeon"),Room(title="5,9", description="dungeon")],[Room(title="4,0", description="dungeon"), Room(title="4,1", description="dungeon"), Room(title="4,2", description="dungeon"),Room(title="4,3", description="dungeon"), Room(title="4,4", description="dungeon"), Room(title="4,5", description="dungeon"),Room(title="4,6", description="dungeon"), Room(title="4,7", description="dungeon"), Room(title="4,8", description="dungeon"),Room(title="4,9", description="dungeon")],[Room(title="3,0", description="dungeon"), Room(title="3,1", description="dungeon"), Room(title="3,2", description="dungeon"),Room(title="3,3", description="dungeon"), Room(title="3,4", description="dungeon"), Room(title="3,5", description="dungeon"),Room(title="3,6", description="dungeon"), Room(title="3,7", description="dungeon"), Room(title="3,8", description="dungeon"),Room(title="3,9", description="dungeon")],[Room(title="2,0", description="dungeon"), Room(title="2,1", description="dungeon"), Room(title="2,2", description="dungeon"),Room(title="2,3", description="dungeon"), Room(title="2,4", description="dungeon"), Room(title="2,5", description="dungeon"),Room(title="2,6", description="dungeon"), Room(title="2,7", description="dungeon"), Room(title="2,8", description="dungeon"),Room(title="2,9", description="dungeon")],[Room(title="1,0", description="dungeon"), Room(title="1,1", description="dungeon"), Room(title="1,2", description="dungeon"),Room(title="1,3", description="dungeon"), Room(title="1,4", description="dungeon"), Room(title="1,5", description="dungeon"),Room(title="1,6", description="dungeon"), Room(title="1,7", description="dungeon"), Room(title="1,8", description="dungeon"),Room(title="1,9", description="dungeon")],[Room(title="0,0", description="dungeon"), Room(title="0,1", description="dungeon"), Room(title="0,2", description="dungeon"),Room(title="0,3", description="dungeon"), Room(title="0,4", description="dungeon"), Room(title="0,5", description="dungeon"),Room(title="0,6", description="dungeon"), Room(title="0,7", description="dungeon"), Room(title="0,8", description="dungeon"),Room(title="0,9", description="dungeon")]]

forest_objects = [[Room(title="9,0", description="forest"), Room(title="9,1", description="forest"), Room(title="9,2", description="forest"),Room(title="9,3", description="forest"), Room(title="9,4", description="forest"), Room(title="9,5", description="forest"),Room(title="9,6", description="forest"), Room(title="9,7", description="forest"), Room(title="9,8", description="forest"),Room(title="9,9", description="forest")],[Room(title="8,0", description="forest"), Room(title="8,1", description="forest"), Room(title="8,2", description="forest"),Room(title="8,3", description="forest"), Room(title="8,4", description="forest"), Room(title="8,5", description="forest"),Room(title="8,6", description="forest"), Room(title="8,7", description="forest"), Room(title="8,8", description="forest"),Room(title="8,9", description="forest")],[Room(title="7,0", description="forest"), Room(title="7,1", description="forest"), Room(title="7,2", description="forest"),Room(title="7,3", description="forest"), Room(title="7,4", description="forest"), Room(title="7,5", description="forest"),Room(title="7,6", description="forest"), Room(title="7,7", description="forest"), Room(title="7,8", description="forest"),Room(title="7,9", description="forest")],[Room(title="6,0", description="forest"), Room(title="6,1", description="forest"), Room(title="6,2", description="forest"),Room(title="6,3", description="forest"), Room(title="6,4", description="forest"), Room(title="6,5", description="forest"),Room(title="6,6", description="forest"), Room(title="6,7", description="forest"), Room(title="6,8", description="forest"),Room(title="6,9", description="forest")],[Room(title="5,0", description="forest"), Room(title="5,1", description="forest"), Room(title="5,2", description="forest"),Room(title="5,3", description="forest"), Room(title="5,4", description="forest"), Room(title="5,5", description="forest"),Room(title="5,6", description="forest"), Room(title="5,7", description="forest"), Room(title="5,8", description="forest"),Room(title="5,9", description="forest")],[Room(title="4,0", description="forest"), Room(title="4,1", description="forest"), Room(title="4,2", description="forest"),Room(title="4,3", description="forest"), Room(title="4,4", description="forest"), Room(title="4,5", description="forest"),Room(title="4,6", description="forest"), Room(title="4,7", description="forest"), Room(title="4,8", description="forest"),Room(title="4,9", description="forest")],[Room(title="3,0", description="forest"), Room(title="3,1", description="forest"), Room(title="3,2", description="forest"),Room(title="3,3", description="forest"), Room(title="3,4", description="forest"), Room(title="3,5", description="forest"),Room(title="3,6", description="forest"), Room(title="3,7", description="forest"), Room(title="3,8", description="forest"),Room(title="3,9", description="forest")],[Room(title="2,0", description="forest"), Room(title="2,1", description="forest"), Room(title="2,2", description="forest"),Room(title="2,3", description="forest"), Room(title="2,4", description="forest"), Room(title="2,5", description="forest"),Room(title="2,6", description="forest"), Room(title="2,7", description="forest"), Room(title="2,8", description="forest"),Room(title="2,9", description="forest")],[Room(title="1,0", description="forest"), Room(title="1,1", description="forest"), Room(title="1,2", description="forest"),Room(title="1,3", description="forest"), Room(title="1,4", description="forest"), Room(title="1,5", description="forest"),Room(title="1,6", description="forest"), Room(title="1,7", description="forest"), Room(title="1,8", description="forest"),Room(title="1,9", description="forest")],[Room(title="0,0", description="forest"), Room(title="0,1", description="forest"), Room(title="0,2", description="forest"),Room(title="0,3", description="forest"), Room(title="0,4", description="forest"), Room(title="0,5", description="forest"),Room(title="0,6", description="forest"), Room(title="0,7", description="forest"), Room(title="0,8", description="forest"),Room(title="0,9", description="forest")]]

ryan_room_objects = [[Room(title="1"), Room(title="2"), Room(title="3"),Room(title="4"), Room(title="5"), Room(title="6"),Room(title="7"), Room(title="8"), Room(title="9"),Room(title="10")],[Room(title="11"), Room(title="12"), Room(title="13"),Room(title="14"), Room(title="15"), Room(title="16"),Room(title="17"), Room(title="18"), Room(title="19"),Room(title="20")],[Room(title="21"), Room(title="22"), Room(title="23"),Room(title="24"), Room(title="25"), Room(title="26"),Room(title="27"), Room(title="28"), Room(title="29"),Room(title="30")],[Room(title="31"), Room(title="32"), Room(title="33"),Room(title="34"), Room(title="35"), Room(title="36"),Room(title="37"), Room(title="38"), Room(title="39"),Room(title="40")],[Room(title="41"), Room(title="42"), Room(title="43"),Room(title="44"), Room(title="45"), Room(title="46"),Room(title="47"), Room(title="48"), Room(title="49"),Room(title="50")],[Room(title="51"), Room(title="52"), Room(title="53"),Room(title="54"), Room(title="55"), Room(title="56"),Room(title="57"), Room(title="58"), Room(title="59"),Room(title="60")],[Room(title="61"), Room(title="62"), Room(title="63"),Room(title="64"), Room(title="65"), Room(title="66"),Room(title="67"), Room(title="68"), Room(title="69"),Room(title="70")],[Room(title="71"), Room(title="72"), Room(title="73"),Room(title="74"), Room(title="75"), Room(title="76"),Room(title="77"), Room(title="78"), Room(title="79"),Room(title="80")],[Room(title="81"), Room(title="82"), Room(title="83"),Room(title="84"), Room(title="85"), Room(title="86"),Room(title="87"), Room(title="88"), Room(title="89"),Room(title="90")],[Room(title="91"), Room(title="92"), Room(title="93"),Room(title="94"), Room(title="95"), Room(title="96"),Room(title="97"), Room(title="98"), Room(title="99"),Room(title="100")]]

boss_room_objects = [[Room(title="1"), Room(title="2"), Room(title="3"),Room(title="4"), Room(title="5"), Room(title="6"),Room(title="7"), Room(title="8"), Room(title="9"),Room(title="10")],[Room(title="11"), Room(title="12"), Room(title="13"),Room(title="14"), Room(title="15"), Room(title="16"),Room(title="17"), Room(title="18"), Room(title="19"),Room(title="20")],[Room(title="21"), Room(title="22"), Room(title="23"),Room(title="24"), Room(title="25"), Room(title="26"),Room(title="27"), Room(title="28"), Room(title="29"),Room(title="30")],[Room(title="31"), Room(title="32"), Room(title="33"),Room(title="34"), Room(title="35"), Room(title="36"),Room(title="37"), Room(title="38"), Room(title="39"),Room(title="40")],[Room(title="41"), Room(title="42"), Room(title="43"),Room(title="44"), Room(title="45"), Room(title="46"),Room(title="47"), Room(title="48"), Room(title="49"),Room(title="50")],[Room(title="51"), Room(title="52"), Room(title="53"),Room(title="54"), Room(title="55"), Room(title="56"),Room(title="57"), Room(title="58"), Room(title="59"),Room(title="60")],[Room(title="61"), Room(title="62"), Room(title="63"),Room(title="64"), Room(title="65"), Room(title="66"),Room(title="67"), Room(title="68"), Room(title="69"),Room(title="70")],[Room(title="71"), Room(title="72"), Room(title="73"),Room(title="74"), Room(title="75"), Room(title="76"),Room(title="77"), Room(title="78"), Room(title="79"),Room(title="80")],[Room(title="81"), Room(title="82"), Room(title="83"),Room(title="84"), Room(title="85"), Room(title="86"),Room(title="87"), Room(title="88"), Room(title="89"),Room(title="90")],[Room(title="91"), Room(title="92"), Room(title="93"),Room(title="94"), Room(title="95"), Room(title="96"),Room(title="97"), Room(title="98"), Room(title="99"),Room(title="100")]]


forest_movements=[[15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [8,13,13,13,9,15,15,15,15,15],[10,14,14,14,11,15,2,15,15,15],[16,14,14,14,14,13,11,15,15,15],[10,14,14,12,14,14,14,13,13,9],[10,14,6,15,10,14,14,14,14,11],[10,11,15,15,7,12,14,14,12,6],[10,11,15,15,15,15,10,11,15,15],[7,12,12,6,15,15,7,12,16,15]]

dungeon_movements=[[15,15,15,15,15,15,15,15,15,15],[15,15,15,15,1,9,15,16,15,2],[15,15,15,15,15,4,8,14,13,11],[15,15,15,15,15,4,10,14,12,6],[15,2,15,8,13,14,14,11,15,15],[15,7,13,14,14,14,14,11,15,15],[15,15,7,14,14,14,14,14,13,9],[15,15,15,7,12,12,14,14,14,11],[15,2,15,15,15,15,10,11,16,4],[15,7,5,5,5,5,12,6,15,0]]

house_movements=[[15,15,15,15,15,15,15,15,15,15],[16,1,13,13,9,15,8,13,13,9],[15,15,10,14,11,15,10,12,12,6],[8,13,14,14,14,13,11,15,4,15],[16,14,14,14,14,14,11,15,4,15],[10,14,14,14,12,12,14,13,14,9],[10,14,14,6,15,15,7,14,14,11],[10,14,11,15,15,15,15,10,14,11],[10,14,14,9,15,15,8,14,14,11],[7,12,12,12,5,5,12,12,12,6]]

basement_movements=[[15,15,8,13,13,13,9,15,15,15],[15,15,10,14,12,12,12,5,3,15],[15,15,10,11,15,15,15,10,14,3],[8,13,14,11,15,16,15,10,14,11],[10,14,14,11,15,4,15,10,14,11],[10,14,14,11,15,4,15,10,14,11],[10,14,14,14,13,14,13,14,14,11],[7,12,14,14,14,14,14,14,14,6],[15,15,7,14,14,14,14,12,6,15],[15,15,15,7,12,12,6,15,15,15]]

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

players=Player.objects.all()
for p in players:
  p.currentRoom=forest_objects[9][0].id
  p.save()

