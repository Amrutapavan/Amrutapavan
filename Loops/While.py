time = 0
while time <= 10:
    print(time)
    time = time + 2
i = 1
while i <= 5:
    print(i)
    i = i +1

login_attempts = 0
while login_attempts < 5:
    print("login_attempts:", login_attempts)
    login_attempts = login_attempts + 1

count = 0
logic_status = True
while logic_status == True:
    print("tri again.")
    count = count + 1
    if count == 4:
        logic_status = False

computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        break
    print(asset)

computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)

xyz = "abcdefg"
print(len(xyz))