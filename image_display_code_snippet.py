imageUrl = "images/{}".format(data[index][7])

load = Image.open(imageUrl)
load = load.resize((200, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

img = Label(image=render)
img.image = render
img.pack()