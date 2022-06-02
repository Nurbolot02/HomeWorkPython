def log(massage) -> None:
    path = 'db.csv'
    with open(path, 'a') as file:
        file.write(f'{massage["chat"]["first_name"]}, {massage["chat"]["id"]}, {massage["text"]}\n')
