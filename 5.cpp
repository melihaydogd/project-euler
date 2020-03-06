#include <iostream>

using namespace std;

int main(){
	
	int number = 2520;
	int flag = 1;
	
	while(1 > 0){
		for(int i = 1; i < 21; i++){
			if((number % i == 0)){
				flag = 0;
			}else{
				flag = 1;
				break;
			}
		}
		if(flag == 0){
			cout << number;
			break;
		}
		number = number + 1;
	}
	
	return 0;
}
