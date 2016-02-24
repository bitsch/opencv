#define F_CPU 14745600
#include<avr/io.h>
#include<avr/interrupt.h>
#include<util/delay.h>
unsigned char data; //to store received data from UDR1
void buzzer_pin_config (void)
{
DDRC = DDRC | 0x08; //Setting PORTC 3 as outpt
PORTC = PORTC & 0xF7; //Setting PORTC 3 logic low to turnoff buzzer
}
void motion_pin_config (void)
{
DDRA = DDRA | 0x0F;
PORTA = PORTA & 0xF0;
DDRL = DDRL | 0x18; //Setting PL3 and PL4 pins as output for PWM generation
PORTL = PORTL | 0x18; //PL3 and PL4 pins are for velocity control using PWM.
}
//Function to initialize ports
void port_init()
{
motion_pin_config();
buzzer_pin_config();
}
void buzzer_on (void)
{
unsigned char port_restore = 0;
port_restore = PINC;
port_restore = port_restore | 0x08;
PORTC = port_restore;
}
void buzzer_off (void)
{
unsigned char port_restore = 0;
port_restore = PINC;
port_restore = port_restore & 0xF7;
PORTC = port_restore;
}
 
SIGNAL(SIG_USART0_DATA) // ISR for Transmission
{
data = 0x38;
UDR0 = data;
data = UDR0;
}
 
//Function To Initialize UART0
// desired baud rate:9600
// actual baud rate:9600 (error 0.0%)
// char size: 8 bit
// parity: Disabled
void uart0_init(void)
{
UCSR0B = 0x00; //disable while setting baud rate
UCSR0A = 0x00;
UCSR0C = 0x06;
// UBRR0L = 0x47; //11059200 Hz
UBRR0L = 0x5F; // 14745600 Hzset baud rate lo
UBRR0H = 0x00; //set baud rate hi
UCSR0B = 0x98;
}
 

//Function To Initialize all The Devices
void init_devices()
{
cli(); //Clears the global interrupts
port_init(); //Initializes all the ports
uart0_init(); //Initailize UART1 for serial communiaction
sei(); //Enables the global interrupts
}
//Main Function
int main(void)
{
init_devices();
while(1);

}