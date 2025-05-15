import random
from mcrcon import MCRcon

# 连接信息
HOST = '192.168.3.100'
PORT = 50032
PASSWORD = '1351912774'

# 读取用户名单
def read_usernames():
    with open('mc_usernames.txt', 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

# 使用 Carpet Mod 生成假人
def spawn_fake_players(rcon, usernames, count=30):
    selected = random.sample(usernames, min(count, len(usernames)))
    for name in selected:
        rcon.command(f"/player {name} spawn")

def main():
    usernames = read_usernames()
    try:
        with MCRcon(HOST, PASSWORD, PORT) as rcon:
            spawn_fake_players(rcon, usernames)
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
