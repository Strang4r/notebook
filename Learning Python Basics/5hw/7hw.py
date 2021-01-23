with open("firms.txt", 'r') as func:
    st = func.readlines()
    new_st = []
    net = []
    loss = []
    firm_net = {}
    all_av_prof = {}
    for i in range(0, len(st)):
        new_st = st[i].split()
        firm_net[new_st[0]] = (int(new_st[2])) - (int(new_st[3]))
        net.append(int(new_st[2]))
        loss.append(int(new_st[3]))
    for i in range(0, len(net)):
        if net[i] > loss[i]:
            av_prof = sum(net) / len(net)
    all_av_prof["average_profit"] = av_prof
    all_dict = [firm_net, all_av_prof]
    print("average profit= ", av_prof)
    print(all_dict)
