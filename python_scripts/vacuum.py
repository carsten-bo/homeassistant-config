
room_living_room = data.get("input_boolean.living_room")
room_bedroom = data.get("input_boolean.bedroom")
room_office = data.get("input_boolean.office")
room_bathroom = data.get("input_boolean.bathroom")
room_hallway = data.get("input_boolean.hallway")
room_hallway_small = data.get("input_boolean.hallway_small")
room_kitchen = data.get("input_boolean.kitchen")

room_list = []
if room_living_room == 'on':
  room_list.append(20)
if room_bedroom == 'on':
  room_list.append(16)
if room_office == 'on':
  room_list.append(1)
if room_bathroom == 'on':
  room_list.append(19)
if room_hallway == 'on':
  room_list.append(17)
if room_hallway_small == 'on':
  room_list.append(21)
if room_kitchen == 'on':
  room_list.append(18)

logger.info("Cleaning rooms: " + str(room_list))

args = {
    "entity_id": "vacuum.xiaomi_vacuum_cleaner",
    "command": "app_segment_clean",
    "params": room_list
    }

hass.services.call("vacuum", "send_command", args)
