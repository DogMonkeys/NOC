#include <iostream>
#include <fstream>
#include <string>
using namespace std;
class Obj{
public:
	char lst[20];
	char n100[20];
	char main_[20];
};

int main(int argc, char const *argv[])
{
	Obj o;
	strcpy(o.lst, argv[1]);
	strcpy(o.n100, argv[2]);
	strcpy(o.main_, argv[3]);
	ofstream Outf(argv[4], ios::out | ios::trunc | ios::binary);
	if (!Outf){
		cout << "err";
		return 2;
	}
	Outf.write((char*)&o, sizeof(o));
	Outf.close();
	cout << "suc";
	return 0;
}
