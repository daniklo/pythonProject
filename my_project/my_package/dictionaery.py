#1
capitals = {
    "Israel": "Jerusalem",
    "China": "Beijing",
    "Argentina": "Buenos Aires",
    "France": "Paris"
}


#2
print(capitals["Israel"])

#3
capitals["England"] = "London"

#4
del capitals["France"]

#5
for count,cap  in capitals.items():
    if cap.startswith("B"):
        print(capitals[count])

        #הפסקה עד 19:20

