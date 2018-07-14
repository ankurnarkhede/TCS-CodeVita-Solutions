#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (auto i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		string wrd;
		getline(cin, wrd);
		int len = wrd.length();
		vector<int> head;
		head.reserve(len);
		head.push_back(0);
		for (int j = 1; j < len; j++) {
			if (wrd[0] == wrd[j]) head.push_back(j);
		}
		int hlen = head.size();
		if (1 == hlen || len == hlen) {
				cout << "Impossible" << endl;
		} else {
			bool possi = false;
			int j = hlen - 1, hjlen;
			while (!possi && 0 < j) {
                                hjlen = len - head[j];
				for (int k = 1; !possi && k < hjlen; k++) possi = wrd[head[j]+k] != wrd[k];
				j--;
			}
			if (possi) 	cout << wrd.substr(0,head[j+1])+ wrd << endl;
			else cout << "Impossible" << endl;
		}
	}
	return 0;
}