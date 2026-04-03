class User:
    def __init__(self, id:int, name:str):
        self.id = id; self.name = name

def map_row(row: dict) -> User:
    return User(int(row['id']), row['name'])

if __name__ == '__main__':
    row = {'id':'2','name':'Bob'}
    u = map_row(row)
    print(u.id, u.name)
