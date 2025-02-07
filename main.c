#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>

#define I2C_DEVICE "/dev/i2c-1" // Change based on your I2C bus (e.g., "/dev/i2c-0")
#define SLAVE_ADDR 0x08         // I2C slave address

int main() {
    int file;
    char buffer[2];

    // Open I2C device
    if ((file = open(I2C_DEVICE, O_RDWR)) < 0) {
        perror("Failed to open I2C bus");
        return 1;
    }

    // Set slave address
    if (ioctl(file, I2C_SLAVE, SLAVE_ADDR) < 0) {
        perror("Failed to set slave address");
        close(file);
        return 1;
    }

    // Write data to the slave
    buffer[0] = 0x01;  // Some data byte
    if (write(file, buffer, 1) != 1) {
        perror("Failed to write to I2C slave");
    }

    // Read data from the slave
    if (read(file, buffer, 1) != 1) {
        perror("Failed to read from I2C slave");
    } else {
        printf("Received: 0x%02X\n", buffer[0]);
    }

    close(file);
    return 0;
}
