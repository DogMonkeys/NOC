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

int main(int argc, char *argv[])
{
    Obj s;       
    ifstream inFile(argv[1], ios::in | ios::binary); //二进制读方式打开
    if(!inFile) {
        cout << "error" <<endl;
        return 1;
    }
    inFile.read((char *)&s, sizeof(s));
    // cout << "您的运动数据如下：" << endl;
    // cout << "跑步：" << s.run << "小时" << endl;
    // cout << "跳绳：" << s.rap << "小时" << endl;
    // cout << "游泳：" << s.swim << "小时" << endl;
    // cout << "走路：" << s.walk << "小时" << endl;
    string l=string("[") + s.lst + ", " + s.n100 + ", " + s.main_  + "]";
    inFile.close();
    cout << l;
    return 0;
}
