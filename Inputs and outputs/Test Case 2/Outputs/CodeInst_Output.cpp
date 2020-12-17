#include <iostream>

#include<stdio.h>

#include <chrono>

#include <fstream>

using namespace std;

using namespace std::chrono;

ofstream Prof("FunctionEventLog_Output.txt");

ofstream Path("CCT_Output.txt");

auto baseLineMilliseconds = high_resolution_clock::now();


int f2(int i) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start f2 Function @" << durationStart << " microS" << endl;



int INSERTEDVALINSTR =  i + 2; 
auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End f2 Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}
int f1(int i) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start f1 Function @" << durationStart << " microS" << endl;



int INSERTEDVALINSTR =  f2(2) + i + 1; 
auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End f1 Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}
int f0(int i) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start f0 Function @" << durationStart << " microS" << endl;



int INSERTEDVALINSTR =  f1(1) + f2(2); 
auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End f0 Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}
int pointed(int i) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start pointed Function @" << durationStart << " microS" << endl;



int INSERTEDVALINSTR =  i; 
auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End pointed Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}
int not_called(int i) {

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start not_called Function @" << durationStart << " microS" << endl;



int INSERTEDVALINSTR =  0; 
auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End not_called Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;
}
int main(int argc, char **argv) {
baseLineMilliseconds = high_resolution_clock::now();

auto  startTime = high_resolution_clock::now();

auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();

Prof << "Start main Function @" << durationStart << " microS" << endl;



    int (*f)(int); // pointer to function

    f0(1);

    f1(1);

    f = pointed;

    if (argc == 1)

        f(1);

    if (argc == 2)

        not_called(1);

int INSERTEDVALINSTR =     0;

auto  endTime = high_resolution_clock::now();

auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();

Prof << "End main Function @" << durationEnd << " microS" << endl;

return INSERTEDVALINSTR ;


}

