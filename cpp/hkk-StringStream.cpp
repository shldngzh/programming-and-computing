#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    // Complete this function
    vector<int> integers;
    int num;
    char ch;
    stringstream ss(str);
    while (!ss.eof()) {
        if (ss >> num){
            integers.push_back(num);
        }
        ss >> ch;
    }
    return integers;
    
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

