#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAX_LEN 8

int main() {
  int16_t x = 0;
  char input_n[MAX_LEN];
  char *endptr;

  if (fgets(input_n, sizeof(input_n), stdin) == NULL) {
    fprintf(stderr, "Error reading 'n'.\n");
    return 1;
  }

  errno = 0;
  long n_long = strtol(input_n, &endptr, 10);
  if (errno != 0 || endptr == input_n || n_long < 0 || n_long > 150) {
    fprintf(stderr, "Invalid value for n.\n");
    return 1;
  }
  uint8_t n = (uint8_t)n_long;

  while (n--) {
    char input_op[MAX_LEN];

    if (fgets(input_op, sizeof(input_op), stdin) == NULL) {
      fprintf(stderr, "Error reading 'op'.\n");
      return 1;
    }

    size_t len = strlen(input_op);
    if (len > 0 && input_op[len - 1] == '\n') {
      input_op[len - 1] = '\0';
    }

    if (strlen(input_op) < 2) {
      fprintf(stderr, "Invalid operation input.\n");
      return 1;
    }
    char op = input_op[1];

    if (op == '+') x++; else x--;
  }

  printf("%d\n", x);
  return 0;
}
