def solution(sizes):
    width, height = 0, 0
    for card in sizes:
        w, h = max(card[0], card[1]), min(card[0], card[1])
        
        if w > width: width = w
        if h > height: height = h

    return width * height