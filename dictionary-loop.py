# looping Dictionary

teman_teman = {
    "mei":"meimei",
    "dhika":"dhidhika",
    "sapta":"sasapta",
    "nawa":"nawawa",
    "sat":"sati",
}

#looping first try (yang keluar adalah keynya)

for teman in teman_teman:
    print(f"nama teman = {teman}")


#operartor untuk  mengambil item /iterable
keys = teman_teman.keys()
for keys in teman_teman.keys():
    print(teman_teman.get(keys))


values = teman_teman.values()
print(values)
for value in teman_teman.values():
    print(value)


for value in teman_teman.values():
    print(value)


items = teman_teman.items()
for item in items:
    print(item)

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")