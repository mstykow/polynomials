#! python3
# Program defines a polynomial class and several methods for manipulating polynomials.

class polynomial():

    # coefficients are of the form [a_0, a_1, a_2, ...]
    # where a_0 + a_1 * x + a_2 * x ** 2 + ...
    coefficients = []

    def __init__(self, coefficients):
        # Remove trailing zeros from coefficient list (needed for some functions below)
        while coefficients[-1] == 0 and len(coefficients) > 1:
            coefficients = coefficients[0:-1]
        self.coefficients = coefficients

    def add(self, other):
        # In order for the addition function to work correctly, both coefficient lists
        # need to be of equal length. Thus, add trailing zeros if needed.
        A = self.coefficients
        B = other.coefficients
        if len(A) > len(B):
            B = B + [0] * (len(A) - len(B))
        elif len(B) > len(A):
            A = A + [0] * (len(B) - len(A))
        result = [A[i] + B[i] for i in range(len(A))]
        return result
    
    def degree(self):
        return len(self.coefficients) - 1

    def derivative(self):
        # Treat special case of constant polynomials first.
        if len(self.coefficients) == 1:
            return [0]
        else:
            result = [(i + 1) * self.coefficients[i + 1] \
                for i in range(len(self.coefficients) - 1)]
            return result

    def evaluate(self, x):
        result = 0
        for i, coefficient in enumerate(self.coefficients):
            result = result + coefficient * x ** i
        return result

    # When comparing two objects, we need to override the default behavior of the
    # equality operator, which would be comparing object IDs, to explicitly compare
    # all the attributes a class contains (__dict__ is a dictionary of all the
    # object's attributes and their values)
    def __eq__(self, other):
        #return self.coefficients == other.coefficients
        return self.__dict__ == other.__dict__

    # Note that the "not equal" operator also needs to be redefined
    def __ne__(self, other):
        return not self == other