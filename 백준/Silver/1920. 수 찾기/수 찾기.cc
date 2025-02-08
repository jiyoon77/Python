#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include <set>

int main() {
    std::set<int> setA;
    int size1, size2, num;

    scanf("%d",&size1);

    for (int i = 0; i < size1; i++) {
        scanf("%d", &num);
        setA.insert(num);
    }

    scanf("%d", &size2);

    for (int i = 0; i < size2; i++) {
        scanf("%d", &num);
        if (setA.find(num) != setA.end()) {
            printf("1\n");
        }
        else {
            printf("0\n");
        }
    }

    return 0;
}