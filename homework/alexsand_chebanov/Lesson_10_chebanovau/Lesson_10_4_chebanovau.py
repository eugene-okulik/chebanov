PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

print({i.split()[0]: int(i.split()[1][:-1]) for i in PRICE_LIST.split('\n')})
