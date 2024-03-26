g, q = map(int, input().split())
girl_group = {}

for _ in range(g):
    name = input()
    member_count = int(input())
    members = []
    for _ in range(member_count):
        member_name = input()
        members.append(member_name)
    members.sort()
    girl_group[name] = members

for _ in range(q):
    quiz_name = input()
    quiz_type = int(input())
    if quiz_type == 0:
        for m in girl_group[quiz_name]:
            print(m)
    else:
        for group_name, members in girl_group.items():
            if quiz_name in members:
                print(group_name)