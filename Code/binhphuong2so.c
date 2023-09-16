#include "stdio.h"
void tongbp(int a, int b)
{
	printf("Nhap so nguyen a:");scanf("%d",&a);
	printf("Nhap so nguyen b:");scanf("%d",&b);
	printf("Tong binh phuong 2 so nguyen %d va %d la:%d",a,b,a*a+b*b);
}
int main()
{
	int a,b,c,d,e,f;
	tongbp(a,b);
}
