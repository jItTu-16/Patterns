"""
n = 3

     * * *
   * * * * *
 * *       * *
 * *       * *
 * *       * *
   * * * * *
     * * *

n = 4

       * * * *
     * * * * * *
   * * * * * * * *
 * * *         * * *
 * * *         * * *
 * * *         * * *
 * * *         * * *
   * * * * * * * *
     * * * * * *
       * * * *

n = 5

         * * * * *
       * * * * * * *
     * * * * * * * * *
   * * * * * * * * * * *
 * * * *           * * * *
 * * * *           * * * *
 * * * *           * * * *
 * * * *           * * * *
 * * * *           * * * *
   * * * * * * * * * * *
     * * * * * * * * *
       * * * * * * *
         * * * * *

"""


def pattern(size):

    for i in range(size - 1):
        print("  " * (size - i - 1) + " *" * (size + 2 * i))

    print(" *" * (size - 1) + "  " * size + " *" * (size - 1))

    for i in range(size - 2):
        print(" *" * (size - 1) + "  " * size + " *" * (size - 1))

    print(" *" * (size - 1) + "  " * size + " *" * (size - 1))

    for i in range(size - 2, -1, -1):
        print("  " * (size - i - 1) + " *" * (size + 2 * i))


size = int(input("Enter size of Octagon :- "))
