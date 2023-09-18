#include "stdio.h"
/*void Nhap(int a,int b)
{
	printf("\nNhap so nguyen thu nhat:");scanf("%d",&a);
	printf("\nNhap so nguyen thu hai:");scanf("%d",&b);
}
*/
void hoan_vi(float *a,float *b)
{
	float c;
	c=*a;
	*a=*b;
	*b=c;
}
int main()
{
	float x,y,z,t;
	printf("Nhap so x:");scanf("%f",&x);
	printf("Nhap so y:");scanf("%f",&y);
	printf("Nhap so z:");scanf("%f",&z);
	printf("Nhap so t:");scanf("%f",&t);
	hoan_vi(&x,&y);
	hoan_vi(&z,&t);
	printf("Gia tri cua x va y sau hoan vi:x=%.2f,y=%.2f",x,y);
	printf("\nGia tri cua z va t sau hoan vi:z=%.2f,t=%.2f",z,t);

}
