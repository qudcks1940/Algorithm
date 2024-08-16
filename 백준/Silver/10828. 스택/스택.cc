#include<iostream>
#include<string>
using namespace std;
int maxsize = 10000;
class stack {
private:
    int* arr;
    int _size;
public:
    stack()
    {
        _size = -1;
        arr = new int[maxsize];
    }
    void push(int x)
    {
        arr[_size] = x;
        _size += 1;
    }
    bool empty()
    {
        if (_size == -1)
            return true;
        else
            return false;
    }
    int pop()
    {
        if (empty() == true)
            return -1;
        else
        {
            int y = arr[_size - 1];
            arr[_size] = 0;
            _size += -1;
            return y;
        }
    }
    int top()
    {
        if (empty() == 1)
            return -1;
        else
            return arr[_size - 1];
    }
    int size()
    {
        return _size + 1;
    }
};

int main() {
    int N;
    cin >> N;
    stack st;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        if (s == "push") {
            int a;
            cin >> a;
            st.push(a);
        }
        else if (s == "pop") {
            cout << st.pop() << "\n";
        }
        else if (s == "empty") {
            cout << st.empty() << "\n";
        }
        else if (s == "size") {
            cout << st.size() << "\n";
        }
        else
            cout << st.top()<<"\n";
    }



    return 0;
}