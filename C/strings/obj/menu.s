	.file	"menu.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"\n--- Limites Inteiros ---"
.LC1:
	.string	"INT_MAX: %d\n"
.LC2:
	.string	"INT_MIN: %d\n"
.LC3:
	.string	"CHAR_MAX: %d\n"
.LC4:
	.string	"CHAR_MIN: %d\n"
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC5:
	.string	"\n--- Limites de Ponto Flutuante ---"
	.section	.rodata.str1.1
.LC7:
	.string	"FLT_MAX: %e\n"
.LC9:
	.string	"FLT_MIN: %e\n"
.LC11:
	.string	"DBL_MAX: %e\n"
.LC13:
	.string	"DBL_MIN: %e\n"
	.text
	.p2align 4
	.globl	exibirLimites
	.type	exibirLimites, @function
exibirLimites:
.LFB54:
	.cfi_startproc
	endbr64
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	leaq	.LC0(%rip), %rdi
	call	puts@PLT
	movl	$2147483647, %edx
	leaq	.LC1(%rip), %rsi
	xorl	%eax, %eax
	movl	$2, %edi
	call	__printf_chk@PLT
	movl	$-2147483648, %edx
	leaq	.LC2(%rip), %rsi
	xorl	%eax, %eax
	movl	$2, %edi
	call	__printf_chk@PLT
	movl	$127, %edx
	leaq	.LC3(%rip), %rsi
	xorl	%eax, %eax
	movl	$2, %edi
	call	__printf_chk@PLT
	movl	$-128, %edx
	leaq	.LC4(%rip), %rsi
	xorl	%eax, %eax
	movl	$2, %edi
	call	__printf_chk@PLT
	leaq	.LC5(%rip), %rdi
	call	puts@PLT
	movl	$2, %edi
	movl	$1, %eax
	movsd	.LC6(%rip), %xmm0
	leaq	.LC7(%rip), %rsi
	call	__printf_chk@PLT
	movl	$2, %edi
	movl	$1, %eax
	movsd	.LC8(%rip), %xmm0
	leaq	.LC9(%rip), %rsi
	call	__printf_chk@PLT
	movl	$2, %edi
	movl	$1, %eax
	movsd	.LC10(%rip), %xmm0
	leaq	.LC11(%rip), %rsi
	call	__printf_chk@PLT
	movl	$2, %edi
	movl	$1, %eax
	movsd	.LC12(%rip), %xmm0
	leaq	.LC13(%rip), %rsi
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	jmp	__printf_chk@PLT
	.cfi_endproc
.LFE54:
	.size	exibirLimites, .-exibirLimites
	.section	.rodata.str1.1
.LC14:
	.string	"Dentro menu..."
	.section	.rodata.str1.8
	.align 8
.LC15:
	.string	"Entrada inv\303\241lida! Por favor, tente novamente."
	.align 8
.LC16:
	.string	"Digite sua string (m\303\241x. %d caracteres): "
	.section	.rodata.str1.1
.LC17:
	.string	"\n"
.LC18:
	.string	"Resultado: %s\n"
.LC19:
	.string	"Encerrando o programa."
	.section	.rodata.str1.8
	.align 8
.LC20:
	.string	"Op\303\247\303\243o inv\303\241lida! Tente novamente."
	.section	.rodata.str1.1
.LC21:
	.string	"\n--- Menu ---"
.LC22:
	.string	"1. Inserir uma string"
	.section	.rodata.str1.8
	.align 8
.LC23:
	.string	"2. Transformar em mai\303\272sculas (uppercase)"
	.align 8
.LC24:
	.string	"3. Transformar em min\303\272sculas (lowercase)"
	.align 8
.LC25:
	.string	"4. Remover espa\303\247os extras (trim)"
	.section	.rodata.str1.1
.LC26:
	.string	"5. Capitalizar palavras"
	.section	.rodata.str1.8
	.align 8
.LC27:
	.string	"6. Exibir limites da linguagem C"
	.section	.rodata.str1.1
.LC28:
	.string	"7. Sair"
.LC29:
	.string	"Escolha uma op\303\247\303\243o: "
.LC30:
	.string	"%d"
	.text
	.p2align 4
	.globl	showMenu
	.type	showMenu, @function
showMenu:
.LFB53:
	.cfi_startproc
	endbr64
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	leaq	.LC21(%rip), %r15
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	leaq	.LC22(%rip), %r14
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	leaq	.LC23(%rip), %r13
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	leaq	.LC24(%rip), %r12
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	leaq	.LC25(%rip), %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	leaq	.L9(%rip), %rbx
	subq	$184, %rsp
	.cfi_def_cfa_offset 240
	movq	%fs:40, %rdi
	movq	%rdi, 168(%rsp)
	leaq	.LC14(%rip), %rdi
	call	puts@PLT
	leaq	28(%rsp), %rax
	pxor	%xmm0, %xmm0
	movq	%rax, (%rsp)
	movaps	%xmm0, 32(%rsp)
	movaps	%xmm0, 48(%rsp)
	movaps	%xmm0, 64(%rsp)
	movaps	%xmm0, 80(%rsp)
	movaps	%xmm0, 96(%rsp)
	movaps	%xmm0, 112(%rsp)
	movaps	%xmm0, 128(%rsp)
	movaps	%xmm0, 144(%rsp)
	.p2align 4
	.p2align 3
.L5:
	movq	%r15, %rdi
	call	puts@PLT
	movq	%r14, %rdi
	call	puts@PLT
	movq	%r13, %rdi
	call	puts@PLT
	movq	%r12, %rdi
	call	puts@PLT
	movq	%rbp, %rdi
	call	puts@PLT
	leaq	.LC26(%rip), %rdi
	call	puts@PLT
	leaq	.LC27(%rip), %rdi
	call	puts@PLT
	leaq	.LC28(%rip), %rdi
	call	puts@PLT
	leaq	.LC29(%rip), %rsi
	movl	$2, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	movq	(%rsp), %rsi
	xorl	%eax, %eax
	leaq	.LC30(%rip), %rdi
	call	__isoc99_scanf@PLT
	cmpl	$1, %eax
	jne	.L25
	movq	stdin(%rip), %rdi
	call	getc@PLT
	cmpl	$7, 28(%rsp)
	ja	.L7
	movl	28(%rsp), %eax
	movslq	(%rbx,%rax,4), %rax
	addq	%rbx, %rax
	notrack jmp	*%rax
	.section	.rodata
	.align 4
	.align 4
.L9:
	.long	.L7-.L9
	.long	.L15-.L9
	.long	.L14-.L9
	.long	.L13-.L9
	.long	.L12-.L9
	.long	.L11-.L9
	.long	.L10-.L9
	.long	.L8-.L9
	.text
	.p2align 4,,10
	.p2align 3
.L8:
	leaq	.LC19(%rip), %rdi
	call	puts@PLT
	movq	168(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L26
	addq	$184, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L10:
	.cfi_restore_state
	xorl	%eax, %eax
	call	exibirLimites
	jmp	.L5
	.p2align 4,,10
	.p2align 3
.L11:
	leaq	32(%rsp), %rdx
	movq	%rdx, %rdi
	movq	%rdx, 8(%rsp)
	call	capitalize@PLT
.L24:
	movq	8(%rsp), %rdx
	leaq	.LC18(%rip), %rsi
	movl	$2, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	jmp	.L5
	.p2align 4,,10
	.p2align 3
.L12:
	leaq	32(%rsp), %rdx
	movq	%rdx, %rdi
	movq	%rdx, 8(%rsp)
	call	trimSpaces@PLT
	jmp	.L24
	.p2align 4,,10
	.p2align 3
.L13:
	leaq	32(%rsp), %rdx
	movq	%rdx, %rdi
	movq	%rdx, 8(%rsp)
	call	lowercase@PLT
	jmp	.L24
	.p2align 4,,10
	.p2align 3
.L14:
	leaq	32(%rsp), %rdx
	movq	%rdx, %rdi
	movq	%rdx, 8(%rsp)
	call	uppercase@PLT
	jmp	.L24
	.p2align 4,,10
	.p2align 3
.L15:
	movl	$127, %edx
	leaq	.LC16(%rip), %rsi
	movl	$2, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	leaq	32(%rsp), %rdi
	movl	$128, %esi
	movq	stdin(%rip), %rdx
	movq	%rdi, 8(%rsp)
	call	fgets@PLT
	movq	8(%rsp), %rdi
	leaq	.LC17(%rip), %rsi
	call	strcspn@PLT
	movb	$0, 32(%rsp,%rax)
	jmp	.L5
	.p2align 4,,10
	.p2align 3
.L25:
	leaq	.LC15(%rip), %rdi
	call	puts@PLT
	.p2align 4
	.p2align 3
.L6:
	movq	stdin(%rip), %rdi
	call	getc@PLT
	cmpl	$10, %eax
	jne	.L6
	jmp	.L5
.L7:
	leaq	.LC20(%rip), %rdi
	call	puts@PLT
	jmp	.L5
.L26:
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE53:
	.size	showMenu, .-showMenu
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC6:
	.long	-536870912
	.long	1206910975
	.align 8
.LC8:
	.long	0
	.long	940572672
	.align 8
.LC10:
	.long	-1
	.long	2146435071
	.align 8
.LC12:
	.long	0
	.long	1048576
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
