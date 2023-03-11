# ------COPY AND POP DICTIONARY-------

# copy dictionary

nama_teman = {
    "a" : "Ilid",
    "b" : "Erlangga",
    "c" : "Cemong",
    "d" : "Dudung",
    "e" : "Bulbul"
}

print(f"nama_teman: {nama_teman}\n")

friends = nama_teman.copy()

nama_teman["a"] = "Bohay"
print(f"nama_teman: {nama_teman}\n")

print(f"friends: {friends}\n")

# pop dictionary --> mentransfer data, nanti data ngilang dari dictionarynya
#ngambil data berdasarkan keynya

databulbul = friends.pop("e")
print(f"databulbul: {databulbul}\n")
print(f"friends: {friends}\n")

# popitem dictionary
# ngambil data terakhir key ama valuenya
dataterakhir = friends.popitem()
print(f"data terakhir: {dataterakhir}\n")
print(f"friends: {friends}\n")
