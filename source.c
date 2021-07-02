#include <stdio.h>
#include <linux/limits.h>
#include "inc.h"

extern int ext; 
int glob;


int updateTab(void) {
	int i = 0;
  
	ext = get_sensor();
	while (tab[i] != ext && i < MAX_INDEX)
	{
		i++;
		ext = get_sensor(); 
	}

	if (i == MAX_INDEX)
		return 0;
	else 
		return 1;

}


void start(void) {
	int count = RTSIG_MAX;
	while (1) {
		count--;
		if (count == 0) {
			count = getCounter();
			if (updateTab())
				count++;
			else { 
				count--;
				break;
			}
		}
	}	
}