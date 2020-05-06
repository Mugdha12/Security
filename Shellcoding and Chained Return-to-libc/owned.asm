BITS 32

section .text
global 	_start

_start:
xor eax, eax
xor ebx, ebx
xor ecx, ecx
xor edx, edx
mov al, 4
mov bl, 1
mov dl, 0x64
push edx
push 0x336e7730
push 0x20337234
push 0x20753059
mov ecx, esp
mov dl, 13
int 0x80 ;
xor eax, eax
xor ebx, ebx
mov al, 1
int 0x80 ; exit(0)





