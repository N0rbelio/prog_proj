def portaslogicas():
    C = Canvas(main, bg="white", height=340, width=590)

    AND = C.create_arc(180, 150, 80, 210, start=0, extent=220, fill="red")

    OR = C.create_arc(180, 20, 80, 210, start=0, extent=220, fill="red")
    C.pack()
