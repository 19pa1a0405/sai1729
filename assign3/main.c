#include <avr/io.h>
#include <util/delay.h>
#include <stdbool.h>
int main (void)

{

bool X=0,Y=0,Z=0,W=0,F=0;

DDRB=0b11110000;

PORTB=0b00001111;

DDRD=0b00000100;


while(1)


{
 X = (PINB & (1 << PINB3)) == (1 << PINB3);

 Y = (PINB & (1 << PINB2)) == (1 << PINB2);

 Z = (PINB & (1 << PINB1)) == (1 << PINB1);

 W = (PINB & (1 << PINB0)) == (1 << PINB0);

 F=(!X&!Z)|(!Y&!Z)|(!X&Y)|(X&Z&W);

 PORTD |= (F << 2);
}
return 0;
}
