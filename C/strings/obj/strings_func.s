	.file	"strings_func.c"
	.text
	.p2align 4
	.globl	uppercase
	.type	uppercase, @function
uppercase:
.LFB16:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movzbl	(%rdi), %ebx
	testb	%bl, %bl
	je	.L1
	movq	%rdi, %rbp
	call	__ctype_toupper_loc@PLT
	.p2align 5
	.p2align 4
	.p2align 3
.L3:
	movq	(%rax), %rdx
	addq	$1, %rbp
	movl	(%rdx,%rbx,4), %edx
	movb	%dl, -1(%rbp)
	movzbl	0(%rbp), %ebx
	testb	%bl, %bl
	jne	.L3
.L1:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE16:
	.size	uppercase, .-uppercase
	.p2align 4
	.globl	lowercase
	.type	lowercase, @function
lowercase:
.LFB17:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movzbl	(%rdi), %ebx
	testb	%bl, %bl
	je	.L10
	movq	%rdi, %rbp
	call	__ctype_tolower_loc@PLT
	.p2align 5
	.p2align 4
	.p2align 3
.L12:
	movq	(%rax), %rdx
	addq	$1, %rbp
	movl	(%rdx,%rbx,4), %edx
	movb	%dl, -1(%rbp)
	movzbl	0(%rbp), %ebx
	testb	%bl, %bl
	jne	.L12
.L10:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE17:
	.size	lowercase, .-lowercase
	.p2align 4
	.globl	trimSpaces
	.type	trimSpaces, @function
trimSpaces:
.LFB18:
	.cfi_startproc
	endbr64
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	movq	%rdi, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movq	%r12, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	call	__ctype_b_loc@PLT
	movq	(%rax), %rbx
	movzbl	(%r12), %eax
	testb	$32, 1(%rbx,%rax,2)
	je	.L19
	.p2align 4
	.p2align 4
	.p2align 3
.L20:
	movzbl	1(%rbp), %eax
	addq	$1, %rbp
	testb	$32, 1(%rbx,%rax,2)
	jne	.L20
.L19:
	movq	%r12, %rdi
	call	strlen@PLT
	leaq	-1(%r12,%rax), %rax
	cmpq	%rax, %rbp
	jb	.L21
	jmp	.L22
	.p2align 5
	.p2align 4,,10
	.p2align 3
.L23:
	subq	$1, %rax
	cmpq	%rbp, %rax
	je	.L22
.L21:
	movzbl	(%rax), %edx
	testb	$32, 1(%rbx,%rdx,2)
	jne	.L23
.L22:
	subq	%rbp, %rax
	movq	%rbp, %rsi
	movq	%r12, %rdi
	movq	%rax, %rbx
	leaq	1(%rax), %rdx
	call	memmove@PLT
	movb	$0, 1(%r12,%rbx)
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE18:
	.size	trimSpaces, .-trimSpaces
	.p2align 4
	.globl	capitalize
	.type	capitalize, @function
capitalize:
.LFB19:
	.cfi_startproc
	endbr64
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movzbl	(%rdi), %ebx
	testb	%bl, %bl
	je	.L29
	movq	%rdi, %rbp
	call	__ctype_b_loc@PLT
	movl	$1, %edx
	movq	%rax, %r12
	jmp	.L34
	.p2align 4,,10
	.p2align 3
.L39:
	testl	%edx, %edx
	je	.L32
	call	__ctype_toupper_loc@PLT
	movq	(%rax), %rax
	movl	(%rax,%rbx,4), %eax
.L33:
	movb	%al, 0(%rbp)
	movzbl	1(%rbp), %ebx
	addq	$1, %rbp
	xorl	%edx, %edx
	testb	%bl, %bl
	je	.L29
.L34:
	movq	(%r12), %rax
	testb	$32, 1(%rax,%rbx,2)
	je	.L39
	movzbl	1(%rbp), %ebx
	addq	$1, %rbp
	movl	$1, %edx
	testb	%bl, %bl
	jne	.L34
.L29:
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L32:
	.cfi_restore_state
	call	__ctype_tolower_loc@PLT
	movq	(%rax), %rax
	movl	(%rax,%rbx,4), %eax
	jmp	.L33
	.cfi_endproc
.LFE19:
	.size	capitalize, .-capitalize
	.ident	"GCC: (Ubuntu 14.2.0-4ubuntu2~24.04) 14.2.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
