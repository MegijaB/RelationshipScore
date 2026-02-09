default score = 0
screen points():
    frame:
        xalign 0.98
        yalign 0.02
        background Frame(Solid("#000000aa"))

        vbox:
            spacing 5
            text "Relationship Status" size 18 color "#ca9dc5"
            text "[score] Points" size 28 color "#d26060"

label start:
    show screen points
    "It's just a test for relationship points"
    "You can get one of two endings"
    menu:
        "You are beautiful today":
            $ score += 10
        "Would be better with makeup":
            $ score -= 10
    menu:
        "You are really interesting person":
            $ score += 10
        "You are boring":
            $ score -= 10
    menu:
        "I would like to know you better":
            $ score += 10
        "I am not interested in you":
            $ score -= 10
    menu:
        "I woud love to meet you again":
            $ score += 10
        "I don't think we have anything in common":
            $ score -= 10

    if score >= 30:
        jump good
    else:
        jump bad

label good:
    hide screen points
    "Ending: They like you"
    "Score: [score] points"
    return

label bad:
    hide screen points
    "Ending: They don't like you"
    "Score: [score] points"
    return