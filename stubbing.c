#include <stdlib.h>

typedef int sint32;

sint32 glob = 0; // global variable, initialized to 0
sint32 foo(sint32* x); // simple declaration

sint32 f(sint32 x) { // f is called by the main generator
  sint32 v;
  sint32 *local_tab;
  sint32 result;

/* === variables === */
  
  v = x; // read the input x
  v = glob;  // read the global variable

/* === functions === */
  
  // User defined function, taking a pointer in parameter
  v = 42;
  result = foo(&v); // an "automatic stub". Here, foo() could modify the pointed data
  result = v;

  // Standard library function, allocating a buffer of 10 ints
  local_tab=(sint32 *) malloc(sizeof(sint32)*10); // not a "dummy" stub but a "standard stub"
  if (local_tab != NULL) {// malloc returns NULL if something goes wrong
    local_tab[glob] = 42; // orange OBAI here since g is "full-range"
  }

  free(local_tab);
  
  return result;

}
