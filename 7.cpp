#include <iostream>

using namespace std;

int main() {

	int *arr;
	arr = new int [10001];
	arr[0] = 2;
	int j = 0;
	int number = 3;
	int flag = 1;
	while(1 > 0) {
		for(int i = 2; i < number; i++) {
			if(number % i == 0) {
				flag = 0;
			}
		}
		if(flag == 1) {
			arr[1+j] = number;
			j = j + 1;
		}
		if(j==10000) {
			break;
		}
		flag = 1;
		number = number + 1;
	}
	cout << arr[10000];

	return 0;
}
