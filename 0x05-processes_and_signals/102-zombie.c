#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop causing the system crash
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates zombie processes
 * Return: 0
 */

int main(void)
{
	int i;
	pid_t z;

	for (i = 0; i < 5; i++)
	{
		z = fork();

		if (!z)
			return (0);
		printf("Zombie process created, PID: %d\n", z);
	}

	infinite_while();
	return (0);
}
