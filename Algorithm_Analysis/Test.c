#include<stdio.h>

int main(){
	int n = 50;
	int sum = 0;
	for(int i = 0 ; i<n ; i++){
		int j =i;
		printf("Task 1 : %d\n",i+1 );
		for(j=n ; j >0 ; j = j/2){
			sum = sum +i;
			printf("Task  2: %d\n",j );

	    }
	}
}