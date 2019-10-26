#include <stdlib.h>

int close_compare(int a, int b, int margin) {
  int difference = abs(abs(a) - abs(b));
  if (difference <=  margin)
    return 0;
  else
    return (a - b)/abs(a - b);
}
