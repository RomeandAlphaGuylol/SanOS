#include<stdio.h>
#include<iostream>
#include <system_error>
#include<unistd.h>
using namespace std;
int main(){
    while (true){

        string txt;
        string cmd;
        txt = "❯❯❯ ";
        cout << txt;
        cin >> cmd;
        if (cmd=="exit()"){
            chdir("..");
            system("python3 main.py");
            system("clear");
        }
        
    }
}