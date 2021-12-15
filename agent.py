import time
from answer import question
import requests

url = "https://speakeasy.ifi.uzh.ch"
username = "bot_393"
password = "9uiyFFWgF_"

# 记录最新消息
room_session = {}  # 房间


def answer(sessionToken, roomId, message):
    ans = question(message)
    r = requests.post(url=url + "/api/room/{}".format(roomId), params={"roomId": roomId, "session": sessionToken},
                      data=ans).json()
    print(r)

def get_room_input_message_record(roomId):
    if room_session.__contains__(roomId):
        return room_session[roomId]
    else:
        room_input_message = {}
        room_session[roomId] = room_input_message
        return room_input_message


# 单个房间信息处理
def list_rooms(sessionToken, room):
    print(room)
    roomId = room['uid']

    room_input_message = get_room_input_message_record(roomId)

    roomInfo = requests.get(url=url + "/api/room/{}/{}".format(roomId, room['startTime']),
                            params={"roomId": roomId, "since": room['startTime'], "session": sessionToken}).json()
    print(roomInfo)

    session_input = room['sessions'][0]
    message_all = roomInfo['messages']
    if len(message_all) > 0:
        last_message = message_all[len(message_all) - 1]
        if session_input != last_message['session']:
            print("未收到新的输入消息呦！")
            return
        print(last_message)
        message_session = last_message['session']
        last_message_ordinal = last_message['ordinal']
        print(f"最新查询到的会话信息标号是:{last_message_ordinal}")

        if room_input_message.__contains__(message_session):
            map_last_message = room_input_message[message_session]
            map_last_message_time = map_last_message['timeStamp']
            map_last_message_ordinal = map_last_message['ordinal']
            map_last_message_content = map_last_message['message']
            message_input_arrived = map_last_message_ordinal < last_message_ordinal
            if message_input_arrived:
                room_input_message[message_session] = last_message
        else:
            room_input_message[message_session] = last_message
            message_input_arrived = True
        print(f"是否有未处理的新消息{message_input_arrived}")

        if message_input_arrived:
            answer(sessionToken, roomId, last_message['message'])
    else:
        print("此房间没有消息")
        return


def start_agent(sessionToken):
    print("\n")
    # 获取房间数目
    chatRooms = requests.get(url=url + "/api/rooms", params={"session": sessionToken}).json()
    chatRooms = chatRooms['rooms']
    if len(chatRooms) > 0:
        for room in chatRooms:
            list_rooms(sessionToken, room)
    else:
        print("not found rooms")


if __name__ == '__main__':
    # BOT用户登录
    r = requests.post(url=url + "/api/login", json={"username": username, "password": password}).json()
    print(r)
    sessionToken = r['sessionToken']
    print(sessionToken)
    while True:
        time.sleep(1)
        start_agent(sessionToken)
