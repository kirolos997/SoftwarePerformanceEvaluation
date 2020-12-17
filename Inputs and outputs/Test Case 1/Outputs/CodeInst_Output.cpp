#include <iostream>

#include<stdio.h>

#include <iostream>

#include<stdio.h>

#include <chrono>

#include <fstream>

using namespace std;

using namespace std::chrono;

ofstream Prof("FunctionEventLog_Output.txt");

ofstream Path("CCT_Output.txt");

auto baseLineMilliseconds = high_resolution_clock::now();


int get_square(int x) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start get_square Function @" << durationStart << " microS" << endl;





int INSERTEDVALINSTR =	  x * x;

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End get_square Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}



int get_cube(int x) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start get_cube Function @" << durationStart << " microS" << endl;





int INSERTEDVALINSTR =	 x * x * x;

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End get_cube Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}





int get_add(int a, int b) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start get_add Function @" << durationStart << " microS" << endl;





int INSERTEDVALINSTR =	 get_square(a) + get_cube(b);

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End get_add Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}

int get_mult(int a, int b) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start get_mult Function @" << durationStart << " microS" << endl;





int INSERTEDVALINSTR =	 get_square(a) * get_cube(b);

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End get_mult Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}







int get_diff(int a, int b) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start get_diff Function @" << durationStart << " microS" << endl;





int INSERTEDVALINSTR =	 get_square(a) - get_cube(b);

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End get_diff Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}







int get_dev(int a, int b) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start get_dev Function @" << durationStart << " microS" << endl;







int INSERTEDVALINSTR =	  get_diff(a, b);

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End get_dev Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}

int main() {
baseLineMilliseconds = high_resolution_clock::now();

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start main Function @" << durationStart << " microS" << endl;





	for (int m = 0; m <= 4; m++) {

		get_mult(2, 2);

	}

	for (int c = 0; c <= 4; c++) {

		get_cube(2);

	}



	for (int a = 0; a <= 7; a++) {

		get_add(2, 2);

	}

	



	for (int j = 0; j <= 5; j++) {

		get_square(2);

	}



	int k = 2;

	get_diff(3, k);

	if(k!=0)

		get_dev(3, k);





int INSERTEDVALINSTR =	 0;

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End main Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}







