import pyopencl as cl
import numpy as np
import itertools

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def main(n):
    # Generiraj osnovnu listu brojeva
    numbers = list(range(1, n + 1))
    num_permutations = factorial(n)

    # OpenCL inicijalizacija
    platform = cl.get_platforms()[0]
    device = platform.get_devices()[0]
    context = cl.Context([device])
    queue = cl.CommandQueue(context)

    kernel_code = """
    __kernel void generate_permutation(__global int *output, 
                                    const int n, 
                                    const int num_permutations,
                                    __local int *elements) {
        int gid = get_global_id(0);
        if (gid >= num_permutations) return;

        // Generiranje permutacije iz globalnog ID-a
        int temp_n = n;
        int idx = gid;

        // Popuni lokalni niz
        for (int i = 0; i < n; i++) {
            elements[i] = i + 1;
        }

        for (int i = 0; i < n; i++) {
            int fact = 1;
            for (int j = 1; j < temp_n; j++) fact *= j;

            int selected_index = idx / fact;
            idx = idx % fact;

            output[gid * n + i] = elements[selected_index];

            // Ukloni iskorišteni element
            for (int j = selected_index; j < temp_n - 1; j++) {
                elements[j] = elements[j + 1];
            }
            temp_n--;
        }
    }
    """

    # Kompajliranje kernela
    program = cl.Program(context, kernel_code).build()

    # Alociranje memorije na GPU-u
    output = np.zeros((num_permutations, n), dtype=np.int8)
    output_buf = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, output.nbytes)

    # Pokretanje kernela
    global_size = (num_permutations,)
    program.generate_permutation(queue, global_size, None, output_buf, np.int8(n), np.int8(num_permutations))

    # Kopiranje rezultata s GPU-a
    cl.enqueue_copy(queue, output, output_buf).wait()

    # Ispis prvih nekoliko permutacija
    print("Prvih 10 permutacija:")
    for i in range(min(10, num_permutations)):
        print(output[i])

if __name__ == "__main__":
    main(11)  # Postavi broj elemenata za permutacije
