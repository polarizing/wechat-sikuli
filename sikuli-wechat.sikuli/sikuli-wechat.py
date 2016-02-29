Region(438,93,403,615)

findAll(Pattern("1456655696928.png").similar(0.80))
last_scan = len(list(getLastMatches()))

for x in range(50):
    findAll(Pattern("1456655696928.png").similar(0.80))
    mm = list(getLastMatches())
    print (mm)
    max_y_val = max([match.getTarget().getY() for match in mm])
    print max_y_val
    for match in mm:
        if match.getTarget().getY() == max_y_val and len(mm) != last_scan:
            last_scan = len(mm)
            click(match)
    if exists("1456654271439.png", 4):
    
        click("1456654271439.png")
        wait("1456654313425.png")
        click("1456654807488.png")
    else:
        if exists("1456655282649.png"):
        
            click("1456655282649.png")
        elif (exists("1456654807488.png", 3) and not exists(Pattern("1456655696928.png").similar(0.72))):
            click("1456654807488.png")
    wait(2)