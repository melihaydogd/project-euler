#include <iostream>
#include <math.h>

using namespace std;

int main() {

	int a = 999;
	int b = 999;
	int number;

	int *arr;
	arr = new int [6];

	while(1 > 0) {
		number = a * b;

		arr[5] = number / 100000;
		number = number % 100000;
		arr[4] = number / 10000;
		number = number % 10000;
		arr[3] = number / 1000;
		number = number % 1000;
		arr[2] = number / 100;
		number = number % 100;
		arr[1] = number / 10;
		number = number % 10;
		arr[0] = number / 1;
		number = number % 1;
		
		if((arr[5] == arr[0]) && (arr[4] == arr[1]) && (arr[3] == arr[2])){
			cout << a << " " << b << "\n";
			cout << a * b;
			break;
		}
		b = b - 1;
		if(b < 900){
			a = a - 1;
			b = 999;
		}

	}

	return 0;
}
