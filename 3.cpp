#include <iostream>

using namespace std;

int main() {

	long long int number = 169;
	int i = 2;
	int j = 0;
	long long int temp = 1;
	int flag = 0;

	int *arr;
	arr = new int [100];

	while (1>0) {
		if(number % i == 0) {
			arr[0+j] = i;
			j = j + 1;
			if(j > 0) {
				temp = temp * arr[0+j-1];
			}
		}
		for(int k = 0; k < j; k++) {
			cout << arr[0+k] << " ";
			if(arr[0+k] == number){
				flag = 1;
				break;
			}
		}
		if(flag == 1){
			break;
		}
		if(temp == number) {
			break;
		}
		i = i + 1;
		cout << "\n";
	}

	return 0;
}
