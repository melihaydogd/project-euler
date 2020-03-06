#include <iostream>

using namespace std;

int main(){

	long long int sum = 0;
	int number;
	int i;
	int j = 0;
	int flag = 1;
	int *arr;
	arr = new int [500000];
	

	for(number = 2; number < 2000000; number++){
		for(i = 0; i < j; i++){
			if((number % arr[i] == 0) && (arr[i] < number / 2)){
				flag = 0;
				break;				
			}
		}
		if(flag == 1){
			arr[0+j] = number;
			sum = sum + number;
			j = j + 1;
		}
		flag = 1;
	}
	cout << sum - 4;

	return 0;
}
