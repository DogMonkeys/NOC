#include <iostream>
#include <fstream>
#include <string>
using namespace std;
class Obj{
public:
	char run[20];
	char rap[20];
	char swim[20];
	char walk[20];
};

int main(int argc, char const *argv[])
{
	Obj o;
	strcpy(o.run, argv[1]);
	strcpy(o.rap, argv[2]);
	strcpy(o.swim, argv[3]);
	strcpy(o.walk, argv[4]);
	ofstream Outf(argv[5], ios::out | ios::trunc | ios::binary);
	if (!Outf){
		cout << "err";
		return 2;
	}
	Outf.write((char*)&o, sizeof(o));
	Outf.close();
	cout << "suc";
	return 0;
}
