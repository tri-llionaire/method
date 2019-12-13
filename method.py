#multiple games implemented in python
#games to implement: blackjack, poker, go fish
#10 is represented as 0
import random
version = '0.0.4-22'
cards = ['spadeA', 'spadeK', 'spadeQ', 'spadeJ', 'spade0', 'spade9', 'spade8', 'spade7', 'spade6', 'spade5', 'spade4', 'spade3', 'spade2', 'heartA', 'heartK', 'heartQ', 'heartJ', 'heart0', 'heart9', 'heart8', 'heart7', 'heart6', 'heart5', 'heart4', 'heart3', 'heart2', 'clubA', 'clubK', 'clubQ', 'clubJ', 'club0', 'club9', 'club8', 'club7', 'club6', 'club5', 'club4', 'club3', 'club2', 'diamondA', 'diamondK', 'diamondQ', 'diamondJ', 'diamond0', 'diamond9', 'diamond8', 'diamond7', 'diamond6', 'diamond5', 'diamond4', 'diamond3', 'diamond2']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
dealt = []
out = 0
game = input('method {}: select a game to play: [g]ofish: '.format(version))


def deal(num, dealt, out):
    d = []
    while num > 0:
        r = random.randint(0, 51)
        if cards[r] not in dealt:
            d.append(cards[r])
            dealt.append(cards[r])
            num -= 1
        else:
            pass
    if len(cards) == 0:
        out = 1
    return d
    return dealt
    return out


def gofish(out):
    print('dealing')
    deck = deal(7, dealt, out)
    bot1 = deal(7, dealt, out)
    bot2 = deal(7, dealt, out)
    bot3 = deal(7, dealt, out)
    out = 0
    m = 0
    win = 0
    while win != 1:
        print('your cards: {}'.format(deck))

        #you
        who = input('ask bot 1, 2, or 3? ')
        what = input('what number? ')
        if ('spade' + what) in deck or ('heart' + what) in deck or ('club' + what) in deck or ('diamond' + what) in deck:
            if who == '1':
                for x in bot1:
                    for y in x:
                        if y == what:
                            deck.append(x)
                            del bot1[bot1.index(x)]
                            print('match: {}'.format(x))
                            m = 1
            elif who == '2':
                for x in bot2:
                    for y in x:
                        if y == what:
                            deck.append(x)
                            del bot2[bot2.index(x)]
                            print('match: {}'.format(x))
                            m = 1
            elif who == '3':
                for x in bot3:
                    for y in x:
                        if y == what:
                            deck.append(x)
                            del bot3[bot3.index(x)]
                            print('match: {}'.format(x))
                            m = 1
            else:
                print('error')
            if m == 0:
                if out == 0:
                    print('go fish')
                    deck.append(deal(1, dealt, out)[0])
                else:
                    print('no more cards')
            m = 0

            #bot1
            who = random.randint(1, 3)
            what = random.choice(numbers)
            if ('spade' + what) in bot1 or ('heart' + what) in bot1 or ('club' + what) in bot1 or ('diamond' + what) in bot1:
                if who == '1':
                    for x in bot2:
                        for y in x:
                            if y == what:
                                bot1.append(x)
                                del bot2[bot2.index(x)]
                                m = 1
                elif who == '2':
                    for x in bot3:
                        for y in x:
                            if y == what:
                                bot1.append(x)
                                del bot3[bot3.index(x)]
                                m = 1
                else:
                    for x in deck:
                        for y in x:
                            if y == what:
                                bot1.append(x)
                                del deck[deck.index(x)]
                                m = 1
                if m == 0:
                    if out == 0:
                        print('bot1 went fishing')
                        bot1.append(deal(1, dealt, out)[0])
                    else:
                        print('out of cards')
                m = 0
            else:
                if out == 0:
                    print('bot1 went fishing')
                    bot1.append(deal(1, dealt, out)[0])
                else:
                    print('out of cards')

            #bot2
            who = random.randint(1, 3)
            what = random.choice(numbers)
            if ('spade' + what) in bot2 or ('heart' + what) in bot2 or ('club' + what) in bot2 or ('diamond' + what) in bot2:
                if who == '1':
                    for x in bot1:
                        for y in x:
                            if y == what:
                                bot2.append(x)
                                del bot1[bot1.index(x)]
                                m = 1
                elif who == '2':
                    for x in bot3:
                        for y in x:
                            if y == what:
                                bot2.append(x)
                                del bot3[bot3.index(x)]
                                m = 1
                else:
                    for x in deck:
                        for y in x:
                            if y == what:
                                bot2.append(x)
                                del deck[deck.index(x)]
                                m = 1
                if m == 0:
                    if out == 0:
                        print('bot2 went fishing')
                        bot2.append(deal(1, dealt, out)[0])
                    else:
                        print('out of cards')
                m = 0
            else:
                if out == 0:
                    print('bot2 went fishing')
                    bot2.append(deal(1, dealt, out)[0])
                else:
                    print('out of cards')

            #bot3
            who = random.randint(1, 3)
            what = random.choice(numbers)
            if ('spade' + what) in bot3 or ('heart' + what) in bot3 or ('club' + what) in bot3 or ('diamond' + what) in bot3:
                if who == '1':
                    for x in bot1:
                        for y in x:
                            if y == what:
                                bot3.append(x)
                                del bot1[bot1.index(x)]
                                m = 1
                elif who == '2':
                    for x in bot2:
                        for y in x:
                            if y == what:
                                bot3.append(x)
                                del bot2[bot2.index(x)]
                                m = 1
                else:
                    for x in deck:
                        for y in x:
                            if y == what:
                                bot3.append(x)
                                del deck[deck.index(x)]
                                m = 1
                if m == 0:
                    if out == 0:
                        print('bot3 went fishing')
                        bot3.append(deal(1, dealt, out)[0])
                    else:
                        print('out of cards')
                m = 0
            else:
                if out == 0:
                    print('bot3 went fishing')
                    bot3.append(deal(1, dealt, out)[0])
                else:
                    print('out of cards')
        else:
            print('not in deck, try again')


if game == 'g':
    gofish(out)
else:
    print('error')