#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - creates a infinite loop
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
 * main - Entry point
 * Return: EXIT_SUCCESS on success, EXIT_FAILURE on fail
 */
int main(void)
{
	pid_t aux = 0;
	size_t i = 0;

	while (i < 5)
	{
		aux = fork();
		if (aux > 0)
		{
			printf("Zombie process created, PID: %i\n", aux);
		}
		else
		{
			exit(EXIT_SUCCESS);
		}
		i++;
	}
	infinite_while();

	return (EXIT_SUCCESS);
}
