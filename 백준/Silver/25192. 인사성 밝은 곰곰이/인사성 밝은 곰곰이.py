N = int(input())
text = [input() for _ in range(N)]

text_combined = "\n".join(text)
users = text_combined.split("ENTER")

setuser = [set(user.strip().split("\n")) for user in users if user.strip() != '']
total = sum(len(user_set) for user_set in setuser)

print(total)