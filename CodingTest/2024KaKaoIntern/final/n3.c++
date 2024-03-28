#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 주어진 주사위 A와 B의 결과 계산
vector<int> calculateScore(vector<vector<int>>& A, vector<vector<int>>& B) {
    vector<int> score(1, 0);
    int maxSum = A.size() * 100;

    // A와 B의 합을 저장할 벡터 초기화
    vector<int> sumA(maxSum + 1, 0), sumB(maxSum + 1, 0);

    sumA[0] = 1;
    for (const auto& dice : A) {
        vector<int> nextSumA(maxSum + 1, 0);
        for (int num : dice) {
            for (int j = 0; j <= maxSum - num; ++j) {
                nextSumA[j + num] += sumA[j];
            }
        }
        sumA = nextSumA;
    }

    sumB[0] = 1;
    for (const auto& dice : B) {
        vector<int> nextSumB(maxSum + 1, 0);
        for (int num : dice) {
            for (int j = 0; j <= maxSum - num; ++j) {
                nextSumB[j + num] += sumB[j];
            }
        }
        sumB = nextSumB;
    }

    // A가 이기는 경우
    for (int i = 0; i <= maxSum; ++i) {
        for (int j = 0; j <= maxSum; ++j) {
            if (i > j) {
                score[0] += sumA[i] * sumB[j];
            }
        }
    }
    return score;
}

// 선택 주사위의 인덱스
vector<int> findIndex(vector<int> selectCase) {
    vector<int> index;
    for (int i = 0; i < selectCase.size(); ++i) {
        if (selectCase[i] == 0) {
            index.push_back(i + 1);
        }
    }
    return index;
}

vector<int> solution(vector<vector<int>> dice) {
    int n = dice.size();
    int maxWin = -1;
    vector<int> selectCase(n, 0);
    vector<int> bestselectCase; 

    // 예외처리
    if (n > 2) {
        fill(selectCase.begin() + n / 2, selectCase.end(), 1);
    } else if (n == 2) {
        selectCase[1] = 1;
    }
    
    do {
        vector<vector<int>> A, B;
        // 선택된 주사위를 A와 B로 나누기
        for (int i = 0; i < n; ++i) {
            if (selectCase[i] == 0) {
                A.push_back(dice[i]);
            } else {
                B.push_back(dice[i]);
            }
        }

        vector<int> score = calculateScore(A, B);

        // max값 찾기
        if (maxWin < score[0]) {
            maxWin = score[0];
            bestselectCase = findIndex(selectCase);
        }

    } while (next_permutation(selectCase.begin(), selectCase.end()));

    return bestselectCase;
}