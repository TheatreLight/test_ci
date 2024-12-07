#include "s21_cat.h"

#include <getopt.h>

#include "../common/parcer.h"

int main(int argc, char **argv) {
    FILE *fp = NULL;
    struct Bool flag = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    struct Bool result_flag = parcer(argc, argv, flag);
    printer(fp, argc, argv, result_flag);
    return 0;
}

void printer(FILE *fp, int argc, char **argv, struct Bool flag) {
    char ch;
    for (int i = 1; i < argc; i++) {
        if (flag.use_flags) break;
        char *str = argv[i];
        if (str[0] != '-') {
            char old = '\n';
            int b = 1;
            int n = 1;
            fp = fopen(argv[i], "r");
            while ((ch = fgetc(fp)) != EOF) {
                if (flag.s) {
                    static int s = 1;
                    if (ch == '\n') {
                        s++;
                        if (s >= 3) continue;
                    } else {
                        s = 0;
                    }
                }
                if (flag.b) {
                    static int b_found = 1;
                    if (ch == '\n') b_found++;
                    if (ch != '\n' && b_found > 0) {
                        printf("%6d\t", b);
                        b++;
                        b_found = 0;
                    }
                } else if (flag.n) {
                    if (old == '\n') {
                        printf("%6d\t", n);
                        n++;
                    }
                    old = ch;
                }
                if (flag.t) {
                    nonprint_printer(ch, flag.t, flag.e, flag.T, flag.E);
                }
                if (flag.T && !flag.t) {
                    if (ch == 9) {
                        nonprint_printer(ch, flag.t, flag.e, flag.T, flag.E);
                        continue;
                    }
                }
                if (flag.e && !flag.t) {
                    nonprint_printer(ch, flag.t, flag.e, flag.T, flag.E);
                }
                if (flag.E && !flag.e) {
                    nonprint_printer(ch, flag.t, flag.e, flag.T, flag.E);
                }
                if (!flag.t && !flag.e) {
                    putchar(ch);
                }
            }
            fclose(fp);
        }
    }
}

/* принтер для непечатаемых символов */

void nonprint_printer(char ch, int flag_t, int flag_e, int flag_T, int flag_E) {
    if ((ch < 9 || ch > 10) && ch < 32 && (flag_t || flag_e)) {
        putchar('^');
        putchar(ch + 64);
    } else if (ch == 127 && (flag_t || flag_e)) {
        putchar('^');
        putchar(63);
    } else if (ch == 9 && (flag_t || flag_T)) {
        putchar('^');
        putchar('I');
    } else if (ch == 10 && (flag_e || flag_E)) {
        putchar('$');
        if (flag_e) putchar('\n');
    } else if (!flag_T && !flag_E) {
        putchar(ch);
    }
}
