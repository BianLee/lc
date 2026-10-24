class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
    
        int daysOfMonth[12]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int arriveAliceMonth {stoi(arriveAlice.substr(0, 2))};
        int arriveAliceDay {stoi(arriveAlice.substr(3,5))};

        int leaveAliceMonth{stoi(leaveAlice.substr(0,2))};
        int leaveAliceDay {stoi(leaveAlice.substr(3,5))};

        int arriveBobMonth {stoi(arriveBob.substr(0, 2))};
        int arriveBobDay {stoi(arriveBob.substr(3,5))};

        int leaveBobMonth{stoi(leaveBob.substr(0,2))};
        int leaveBobDay {stoi(leaveBob.substr(3,5))};


        int alice[2]{0, 0}; 
        int bob[2]{0,0};

        for (int i = 0; i < arriveAliceMonth-1; i++) {
            alice[0] += daysOfMonth[i];
        }
        alice[0] += arriveAliceDay;
        for (int i = 0; i < leaveAliceMonth-1; i++) {
            alice[1] += daysOfMonth[i];
        }
        alice[1] += leaveAliceDay;

        
        for (int i = 0; i < arriveBobMonth-1; i++) {
            bob[0] += daysOfMonth[i];
        }
        bob[0] += arriveBobDay;
        for (int i = 0; i < leaveBobMonth-1; i++) {
            bob[1] += daysOfMonth[i];
        }
        bob[1] += leaveBobDay;

        cout << alice[0] << ", " << alice[1] << '\n';
        cout << bob[0] << ", " << bob[1] << '\n';

        // alice: 227, 230
        // bob: 228, 231

        int overlapStart = max(alice[0], bob[0]);
        int overlapEnd = min(alice[1], bob[1]);
        
        // overlapStart: 228, overlapEnd: 230

        if ((overlapEnd - overlapStart + 1) > 0) {
            return overlapEnd - overlapStart + 1; 
        }
        
        return 0;


        return 0;
    }
};
