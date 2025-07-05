class User:
  def __init__(self, uname, name, email):
    self.username = uname
    self.name = name
    self.email = email
  
  def show(self):
    return f"Username: {self.username} | Name: {self.name} | Email: {self.email}"


class UserDatabase:
  def __init__(self):
    self.users = []

  def insert(self, user):
    i = 0
    while i < len(self.users):
      if self.users[i].username > user.username:
        break
    
      i += 1
    self.users.insert(i, user)

    print(f"{user.username} inserted...")
    
  def find(self, username):
    print(f"Finding {username}")
    for user in self.users:
      if user.username == username:
        return user
    
    return 'Not found'
  
  def update(self, user):
    target = self.find(user.username)
    if target == 'Not found': 
      print("No such user present")
      return
    else: 
      target.name, target.email = user.name, user.email
      return
    
  def list_all(self):
    return self.users


class BSTNode:
  pass




user1 = User('user1', 'Kolo', 'userEmail1@mail.com')
user2 = User('user2', 'Muani', 'userEmail2@mail.com')
user3 = User('user3', 'Jinga', 'userEmail3@mail.com')

print(user1.show())

print("Inserting users...")
user_db = UserDatabase()
user_db.insert(user1)
user_db.insert(user2)
user_db.insert(user3)
print("Users Inserted...")

# Inserting
print("Add a User...")
user_db.insert(User(input("Enter username: "), input("Enter name: "), input("Enter email: ")))

print("\nListing All...\n")
users = user_db.list_all()
for i in users:
  print(i.show())

# Finding
print()
found_user = user_db.find(input("Enter username to find: "))
if found_user == "Not found":
  print("---No Such User---")
else:
  print(found_user.show())

