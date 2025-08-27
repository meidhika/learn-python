teman_teman = {
    "mei":"meimei",
    "dhika":"dhidhika",
    "sapta":"sasapta",
    "nawa":"nawawa",
    "sat":"sati",
}

friends = teman_teman.copy()
# print("friends",friends)

# teman_teman["mei"] = "meidhika"
# print("teman teman",teman_teman)

#pop dictionary berdasarkan (key)
data_mei = friends.pop("mei")
print("data mei",data_mei)
print("friends",friends)

#popitem, data yang terakhir.
data_terakhir = friends.popitem()
print("data terakhir",data_terakhir)
print("friends",friends)