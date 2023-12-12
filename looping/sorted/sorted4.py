tweets="what a game , hats off to both teams . well done @benstoke38 @patcummins30 you have bought test cricket back to life love tst cricket @thebarmyary @cricketaus"

words=tweets.split(" ")
for w in words:
    if w.startswith("@"):
        print(w)

