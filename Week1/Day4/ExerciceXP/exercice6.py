def make_shirt(size="large" , texte="I love python"):
    print(f"The size of the shirt is{size} andthe text is{texte}: ")
    make_shirt(size="large")
    make_shirt(size="Medium")
    make_shirt(size="small",texte="Hello world")
    #bonus
    make_shirt(text="Python is awesome", size="large")

