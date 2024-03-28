#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int coin, vector<int> cards) {
    int target = cards.size() + 1;
    vector<int> myCards;
    int round = 0;
    int myPairCount = 0;

    for (int i = 0; i < cards.size() / 3; i++) {
        myCards.push_back(cards[i]);
    }
    
    // 초기에 target을 만족하는 카드 페어 제거
    bool pairFound;
    do {
        pairFound = false;
        for (int i = 0; i < myCards.size(); i++) {
            auto it = find(myCards.begin() + i + 1, myCards.end(), target - myCards[i]);
            if (it != myCards.end()) {
                myCards.erase(it);
                myCards.erase(myCards.begin() + i);
                pairFound = true;
                myPairCount++;
                break;
            }
        }
    } while (pairFound);

    myCards.clear();
    for (int i = 0; i < cards.size() / 3; i++) {
        myCards.push_back(cards[i]);
    }
    cards.erase(cards.begin(), cards.begin() + cards.size() / 3);

    int buyableCoin = (coin - (myCards.size() - myPairCount * 2)) / 2;

    while (!myCards.empty()) {
        round++;

        if (coin > 0) {
            for (int i = 0; i < 2 && !cards.empty(); i++) {
                if (find(myCards.begin(), myCards.end(), target - cards[0]) !=
                    myCards.end()) {
                    myCards.push_back(cards[0]);
                    coin--;
                } else if (buyableCoin > 0) {
                    myCards.push_back(cards[0]);
                    coin--;
                    buyableCoin--;
                } else if (myPairCount == 0 && i == 0 && coin > 1 && cards[0] + cards[1] == target) {
                    myCards.push_back(cards[0]);
                    myCards.push_back(cards[1]);
                    coin -= 2;
                    cards.erase(cards.begin(), cards.begin() + 2);
                    break;
                }
                cards.erase(cards.begin());
            }
        } else {
            cards.erase(cards.begin(), cards.begin() + 2);
        }

        pairFound = false;
        for (int i = 0; i < myCards.size(); i++) {
            auto it = find(myCards.begin() + i + 1, myCards.end(), target - myCards[i]);
            if (it != myCards.end()) {
                myCards.erase(it);
                myCards.erase(myCards.begin() + i);
                pairFound = true;
                break;
            }
        }

        // 더 이상 제거할 카드가 없으면 게임 종료
        if (!pairFound) return round;
    }
    round++;

    return round;
}