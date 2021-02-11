import pbfplayer as p

#frame loop !1!
while True:
    p.screen()
    print(p.time.ctime(p.time.time()))
    #if input requested
    if p.taking_inp == True:
        p.in_channel=input("> ")
    p.sleep(0.5)
    p.clear()
    