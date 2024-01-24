#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

void calculateScoreRecursive(vector<vector<int>>& A, vector<vector<int>>& B,
                             int indexA, int indexB, int sumA, int sumB,
                             vector<int>& score) {
    if (indexA == A.size() && indexB == B.size()) {
        if (sumA > sumB)
            ++score[0];
        // else if (sumA < sumB)
        //     ++score[2];
        // else
        //     ++score[1];
        return;
    }

    if (indexA < A.size()) {
        for (int i = 0; i < 6; ++i) {
            calculateScoreRecursive(A, B, indexA + 1, indexB, sumA + A[indexA][i],
                                sumB, score);
        }
    }

    if (indexB < B.size()) {
        for (int i = 0; i < 6; ++i) {
            calculateScoreRecursive(A, B, indexA, indexB + 1, sumA,
                                sumB + B[indexB][i], score);
        }
    }
}

vector<int> calculateScore(vector<vector<int>>& A, vector<vector<int>>& B) {
    vector<int> score(1, 0);
    calculateScoreRecursive(A, B, 0, 0, 0, 0, score);
    return score;
}

vector<int> findIndex(vector<int> selection) {
    vector<int> index;
    for (int i = 0; i < selection.size(); ++i) {
        if (selection[i] == 0) {
            index.push_back(i + 1);
        }
    }
    return index;
}

vector<int> solution(vector<vector<int>> dice) {
    int n = dice.size();
    vector<int> selection(n, 0);
    int maxWin = -1;
    vector<int> bestSelection;

    if (n > 2) {
        fill(selection.begin() + n / 2, selection.end(), 1);
    } else if (n == 2) {
        selection[1] = 1;
    }
        
    do {
        vector<vector<int>> A, B;
        for (int i = 0; i < n; ++i) {
            if (selection[i] == 0) {
                A.push_back(dice[i]);
            } else {
                B.push_back(dice[i]);
            }
        }

        vector<int> score = calculateScore(A, B);

        if (maxWin < score[0]) {
            maxWin = score[0];
            bestSelection = findIndex(selection);
        }

    } while (next_permutation(selection.begin(), selection.end()));

    return bestSelection;
}