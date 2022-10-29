;driving the display decoder
.include "/home/sai/codes/m328Pdef.inc"

Start:
 ldi r30,0b11110000;     \\identifying input pins 8,9,10,11
 out DDRB,r30;            \\declaring pins as input
 ldi r30,0b11111111;
 out PORTB,r30;            \\activating internal-pullup for pins 2,3,4,5
 in r30,PINB
 ldi r16,0b00000100;        \\identifying output pin 2
 out DDRD,r16;
 ldi r17,0b00000001
 ldi r18,0b00000001
 ldi r19,0b00000001
 ldi r20,0b00000001

 AND r17,r30          ;r17=W
 LSR  r30
 AND r18,r30           ;r18=Z
 LSR r30
 AND r19,r30           ;r19=Y
 LSR r30
 AND r20,r30           ;r20=X

 ldi r21,0b00000001
 eor r21,r17           ;r21=W'

ldi r22,0b00000001
 eor r22,r18           ;r22=Z'

 ldi r23,0b00000001
 eor r23,r19           ;r23=Y'
 
 ldi r24,0b00000001    ;r24=X'
 eor r24,r20

 MOV r0,r22            ;r0=Z'
 AND r0,r24            ;r0=X'Z'
 MOV r1,r19            ;r1=Y
 AND r1,r24            ;r1=X'Y
 MOV r2,r23            ;r2=Y'
 AND r2,r22            ;r2=Y'Z'
 MOV r3,r20            ;r3=X
 AND r3,r17            ;r3=XW
 AND r3,r18            ;r3=XZW
 OR  r3,r2             ;r2=X'Z'+Y'Z'
 OR  r3,r1             ;r0=X'Y+XZW
 OR  r3,r0             ;r0=X'Z'+Y'Z'+X'Y+XZW

LSL r3               ;r0=000000y0
LSL r3               ;r0=00000y00
out PortD,r3

rjmp Start
