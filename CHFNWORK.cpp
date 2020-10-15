#include <iostream>
using namespace std;

int main() {

	int t;
	cin >> t;
	while (t--) {
		int n, k;
		bool flag;
		int sum = 0, count = 1;
		cin >> n >> k;
		int *arr = new int[n];
		for (int i = 0;i < n;i++) {
			cin >> arr[i];
		}
		int sumarr = 0;
		for (int i = 0;i < n;i++) {
			sumarr += arr[i];
		}
		for (int i = 0;i < n;i++) {
			if (arr[i] > k) {
				flag = false;
				cout << -1 << endl;
				break;
			}
			if ((arr[i]) <= k) {
				flag = true;
				sum += arr[i];
				if (sum <= k && i == (n - 1) && sum <= sumarr) {
					flag = false;
					cout << count << endl;
					break;
				}
				else if (sum <= k && i != (n - 1)) {
					continue;
				}
				else if (sum == k && i != (n - 1)) {
					count++;
					sum = 0;
				}
				else if (sum > k) {
					count++;
					sum = arr[i];
				}
			}
		}
		if (flag != false)
			cout << count << endl;
	}
	return 0;
}
