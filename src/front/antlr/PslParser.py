# Generated from Psl.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 57, 640, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 2, 20,
        7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2, 26, 7, 26,
        2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 2, 30, 7, 30, 2, 31, 7, 31, 2, 32, 7, 32, 2, 33,
        7, 33, 2, 34, 7, 34, 2, 35, 7, 35, 2, 36, 7, 36, 2, 37, 7, 37, 2, 38, 7, 38, 2, 39, 7, 39,
        2, 40, 7, 40, 2, 41, 7, 41, 2, 42, 7, 42, 2, 43, 7, 43, 2, 44, 7, 44, 2, 45, 7, 45, 2, 46,
        7, 46, 2, 47, 7, 47, 2, 48, 7, 48, 2, 49, 7, 49, 2, 50, 7, 50, 1, 0, 3, 0, 104, 8, 0, 1, 1,
        3, 1, 107, 8, 1, 1, 1, 4, 1, 110, 8, 1, 11, 1, 12, 1, 111, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,
        2, 1, 2, 3, 2, 121, 8, 2, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 127, 8, 3, 1, 3, 3, 3, 130, 8, 3, 1,
        3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 4, 3, 4, 138, 8, 4, 1, 4, 1, 4, 1, 4, 1, 5, 1, 5, 1, 5, 3, 5, 146,
        8, 5, 1, 5, 3, 5, 149, 8, 5, 1, 6, 1, 6, 3, 6, 153, 8, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6,
        3, 6, 161, 8, 6, 1, 6, 3, 6, 164, 8, 6, 1, 6, 3, 6, 167, 8, 6, 1, 6, 1, 6, 1, 6, 1, 7, 1, 7,
        1, 7, 3, 7, 175, 8, 7, 1, 7, 1, 7, 3, 7, 179, 8, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 3, 8, 186,
        8, 8, 1, 8, 1, 8, 1, 8, 1, 9, 1, 9, 3, 9, 193, 8, 9, 1, 9, 1, 9, 1, 10, 1, 10, 1, 10, 1, 10,
        1, 11, 1, 11, 1, 11, 3, 11, 204, 8, 11, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13,
        1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14, 3, 14, 223, 8, 14,
        1, 15, 1, 15, 1, 15, 5, 15, 228, 8, 15, 10, 15, 12, 15, 231, 9, 15, 1, 16, 5, 16, 234,
        8, 16, 10, 16, 12, 16, 237, 9, 16, 1, 17, 1, 17, 3, 17, 241, 8, 17, 1, 17, 1, 17, 1, 17,
        3, 17, 246, 8, 17, 1, 17, 5, 17, 249, 8, 17, 10, 17, 12, 17, 252, 9, 17, 1, 17, 3, 17,
        255, 8, 17, 1, 17, 1, 17, 1, 18, 1, 18, 3, 18, 261, 8, 18, 1, 18, 1, 18, 1, 18, 3, 18, 266,
        8, 18, 1, 18, 5, 18, 269, 8, 18, 10, 18, 12, 18, 272, 9, 18, 1, 18, 3, 18, 275, 8, 18,
        1, 18, 1, 18, 1, 19, 1, 19, 3, 19, 281, 8, 19, 1, 19, 1, 19, 1, 19, 3, 19, 286, 8, 19, 1,
        19, 5, 19, 289, 8, 19, 10, 19, 12, 19, 292, 9, 19, 3, 19, 294, 8, 19, 1, 19, 3, 19, 297,
        8, 19, 1, 19, 1, 19, 1, 20, 1, 20, 3, 20, 303, 8, 20, 1, 21, 1, 21, 3, 21, 307, 8, 21, 1,
        21, 1, 21, 1, 21, 3, 21, 312, 8, 21, 1, 21, 5, 21, 315, 8, 21, 10, 21, 12, 21, 318, 9,
        21, 3, 21, 320, 8, 21, 1, 21, 3, 21, 323, 8, 21, 1, 21, 1, 21, 1, 22, 1, 22, 3, 22, 329,
        8, 22, 1, 22, 1, 22, 1, 22, 1, 22, 3, 22, 335, 8, 22, 1, 23, 1, 23, 1, 23, 1, 23, 1, 24,
        1, 24, 1, 24, 1, 24, 3, 24, 345, 8, 24, 1, 24, 5, 24, 348, 8, 24, 10, 24, 12, 24, 351,
        9, 24, 1, 25, 1, 25, 3, 25, 355, 8, 25, 1, 25, 1, 25, 1, 25, 3, 25, 360, 8, 25, 1, 25, 5,
        25, 363, 8, 25, 10, 25, 12, 25, 366, 9, 25, 3, 25, 368, 8, 25, 1, 25, 3, 25, 371, 8, 25,
        1, 25, 1, 25, 1, 26, 1, 26, 3, 26, 377, 8, 26, 1, 26, 1, 26, 1, 26, 3, 26, 382, 8, 26, 1,
        26, 5, 26, 385, 8, 26, 10, 26, 12, 26, 388, 9, 26, 3, 26, 390, 8, 26, 1, 26, 3, 26, 393,
        8, 26, 1, 26, 1, 26, 1, 27, 1, 27, 3, 27, 399, 8, 27, 1, 27, 1, 27, 1, 27, 3, 27, 404, 8,
        27, 1, 27, 5, 27, 407, 8, 27, 10, 27, 12, 27, 410, 9, 27, 3, 27, 412, 8, 27, 1, 27, 3,
        27, 415, 8, 27, 1, 27, 1, 27, 1, 28, 1, 28, 3, 28, 421, 8, 28, 1, 28, 1, 28, 1, 28, 3, 28,
        426, 8, 28, 1, 28, 5, 28, 429, 8, 28, 10, 28, 12, 28, 432, 9, 28, 3, 28, 434, 8, 28, 1,
        28, 3, 28, 437, 8, 28, 1, 28, 1, 28, 1, 29, 1, 29, 3, 29, 443, 8, 29, 1, 29, 3, 29, 446,
        8, 29, 1, 29, 1, 29, 1, 30, 1, 30, 1, 30, 3, 30, 453, 8, 30, 1, 31, 4, 31, 456, 8, 31, 11,
        31, 12, 31, 457, 1, 32, 1, 32, 3, 32, 462, 8, 32, 1, 33, 1, 33, 1, 33, 1, 33, 1, 33, 3,
        33, 469, 8, 33, 1, 33, 3, 33, 472, 8, 33, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34, 3, 34, 479,
        8, 34, 1, 34, 1, 34, 1, 34, 5, 34, 484, 8, 34, 10, 34, 12, 34, 487, 9, 34, 1, 35, 1, 35,
        3, 35, 491, 8, 35, 1, 36, 1, 36, 1, 36, 3, 36, 496, 8, 36, 1, 37, 4, 37, 499, 8, 37, 11,
        37, 12, 37, 500, 1, 38, 1, 38, 3, 38, 505, 8, 38, 1, 38, 1, 38, 1, 38, 3, 38, 510, 8, 38,
        1, 38, 5, 38, 513, 8, 38, 10, 38, 12, 38, 516, 9, 38, 3, 38, 518, 8, 38, 1, 38, 3, 38,
        521, 8, 38, 1, 38, 1, 38, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 3, 39, 532, 8,
        39, 1, 40, 1, 40, 1, 40, 3, 40, 537, 8, 40, 1, 40, 3, 40, 540, 8, 40, 1, 41, 1, 41, 1, 41,
        1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 3, 42, 553, 8, 42, 1, 43, 1, 43,
        1, 43, 3, 43, 558, 8, 43, 1, 44, 1, 44, 1, 44, 1, 44, 1, 44, 1, 44, 1, 44, 3, 44, 567, 8,
        44, 1, 45, 1, 45, 3, 45, 571, 8, 45, 1, 46, 1, 46, 1, 47, 1, 47, 1, 47, 1, 47, 1, 47, 3,
        47, 580, 8, 47, 1, 47, 1, 47, 1, 47, 3, 47, 585, 8, 47, 1, 47, 1, 47, 1, 47, 1, 47, 1, 47,
        3, 47, 592, 8, 47, 1, 47, 1, 47, 1, 47, 5, 47, 597, 8, 47, 10, 47, 12, 47, 600, 9, 47,
        3, 47, 602, 8, 47, 1, 48, 1, 48, 1, 48, 1, 48, 1, 48, 5, 48, 609, 8, 48, 10, 48, 12, 48,
        612, 9, 48, 1, 48, 1, 48, 3, 48, 616, 8, 48, 1, 48, 1, 48, 1, 48, 3, 48, 621, 8, 48, 1,
        48, 1, 48, 1, 48, 1, 48, 1, 48, 1, 48, 1, 48, 3, 48, 630, 8, 48, 3, 48, 632, 8, 48, 1, 49,
        1, 49, 3, 49, 636, 8, 49, 1, 50, 1, 50, 1, 50, 0, 1, 68, 51, 0, 2, 4, 6, 8, 10, 12, 14, 16,
        18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
        62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 0, 3,
        1, 0, 9, 13, 1, 0, 25, 26, 1, 0, 34, 36, 711, 0, 103, 1, 0, 0, 0, 2, 109, 1, 0, 0, 0, 4, 120,
        1, 0, 0, 0, 6, 122, 1, 0, 0, 0, 8, 134, 1, 0, 0, 0, 10, 142, 1, 0, 0, 0, 12, 150, 1, 0, 0,
        0, 14, 171, 1, 0, 0, 0, 16, 182, 1, 0, 0, 0, 18, 190, 1, 0, 0, 0, 20, 196, 1, 0, 0, 0, 22,
        203, 1, 0, 0, 0, 24, 205, 1, 0, 0, 0, 26, 211, 1, 0, 0, 0, 28, 217, 1, 0, 0, 0, 30, 229,
        1, 0, 0, 0, 32, 235, 1, 0, 0, 0, 34, 238, 1, 0, 0, 0, 36, 258, 1, 0, 0, 0, 38, 278, 1, 0,
        0, 0, 40, 302, 1, 0, 0, 0, 42, 304, 1, 0, 0, 0, 44, 326, 1, 0, 0, 0, 46, 336, 1, 0, 0, 0,
        48, 340, 1, 0, 0, 0, 50, 352, 1, 0, 0, 0, 52, 374, 1, 0, 0, 0, 54, 396, 1, 0, 0, 0, 56, 418,
        1, 0, 0, 0, 58, 440, 1, 0, 0, 0, 60, 449, 1, 0, 0, 0, 62, 455, 1, 0, 0, 0, 64, 461, 1, 0,
        0, 0, 66, 468, 1, 0, 0, 0, 68, 478, 1, 0, 0, 0, 70, 488, 1, 0, 0, 0, 72, 495, 1, 0, 0, 0,
        74, 498, 1, 0, 0, 0, 76, 502, 1, 0, 0, 0, 78, 531, 1, 0, 0, 0, 80, 536, 1, 0, 0, 0, 82, 541,
        1, 0, 0, 0, 84, 552, 1, 0, 0, 0, 86, 557, 1, 0, 0, 0, 88, 566, 1, 0, 0, 0, 90, 570, 1, 0,
        0, 0, 92, 572, 1, 0, 0, 0, 94, 601, 1, 0, 0, 0, 96, 631, 1, 0, 0, 0, 98, 633, 1, 0, 0, 0,
        100, 637, 1, 0, 0, 0, 102, 104, 3, 2, 1, 0, 103, 102, 1, 0, 0, 0, 103, 104, 1, 0, 0, 0,
        104, 1, 1, 0, 0, 0, 105, 107, 3, 74, 37, 0, 106, 105, 1, 0, 0, 0, 106, 107, 1, 0, 0, 0,
        107, 108, 1, 0, 0, 0, 108, 110, 3, 4, 2, 0, 109, 106, 1, 0, 0, 0, 110, 111, 1, 0, 0, 0,
        111, 109, 1, 0, 0, 0, 111, 112, 1, 0, 0, 0, 112, 3, 1, 0, 0, 0, 113, 121, 3, 6, 3, 0, 114,
        121, 3, 8, 4, 0, 115, 121, 3, 12, 6, 0, 116, 121, 3, 14, 7, 0, 117, 121, 3, 16, 8, 0, 118,
        121, 3, 18, 9, 0, 119, 121, 3, 20, 10, 0, 120, 113, 1, 0, 0, 0, 120, 114, 1, 0, 0, 0, 120,
        115, 1, 0, 0, 0, 120, 116, 1, 0, 0, 0, 120, 117, 1, 0, 0, 0, 120, 118, 1, 0, 0, 0, 120,
        119, 1, 0, 0, 0, 121, 5, 1, 0, 0, 0, 122, 123, 5, 42, 0, 0, 123, 126, 3, 22, 11, 0, 124,
        125, 5, 1, 0, 0, 125, 127, 3, 86, 43, 0, 126, 124, 1, 0, 0, 0, 126, 127, 1, 0, 0, 0, 127,
        129, 1, 0, 0, 0, 128, 130, 5, 2, 0, 0, 129, 128, 1, 0, 0, 0, 129, 130, 1, 0, 0, 0, 130,
        131, 1, 0, 0, 0, 131, 132, 3, 60, 30, 0, 132, 133, 3, 72, 36, 0, 133, 7, 1, 0, 0, 0, 134,
        135, 5, 43, 0, 0, 135, 137, 3, 22, 11, 0, 136, 138, 5, 2, 0, 0, 137, 136, 1, 0, 0, 0, 137,
        138, 1, 0, 0, 0, 138, 139, 1, 0, 0, 0, 139, 140, 3, 60, 30, 0, 140, 141, 3, 72, 36, 0,
        141, 9, 1, 0, 0, 0, 142, 145, 5, 47, 0, 0, 143, 146, 3, 100, 50, 0, 144, 146, 3, 36, 18,
        0, 145, 143, 1, 0, 0, 0, 145, 144, 1, 0, 0, 0, 146, 148, 1, 0, 0, 0, 147, 149, 5, 50, 0,
        0, 148, 147, 1, 0, 0, 0, 148, 149, 1, 0, 0, 0, 149, 11, 1, 0, 0, 0, 150, 152, 3, 30, 15,
        0, 151, 153, 3, 10, 5, 0, 152, 151, 1, 0, 0, 0, 152, 153, 1, 0, 0, 0, 153, 154, 1, 0, 0,
        0, 154, 155, 3, 32, 16, 0, 155, 156, 5, 44, 0, 0, 156, 157, 3, 100, 50, 0, 157, 160,
        3, 38, 19, 0, 158, 159, 5, 1, 0, 0, 159, 161, 3, 86, 43, 0, 160, 158, 1, 0, 0, 0, 160,
        161, 1, 0, 0, 0, 161, 163, 1, 0, 0, 0, 162, 164, 5, 2, 0, 0, 163, 162, 1, 0, 0, 0, 163,
        164, 1, 0, 0, 0, 164, 166, 1, 0, 0, 0, 165, 167, 5, 50, 0, 0, 166, 165, 1, 0, 0, 0, 166,
        167, 1, 0, 0, 0, 167, 168, 1, 0, 0, 0, 168, 169, 3, 58, 29, 0, 169, 170, 3, 72, 36, 0,
        170, 13, 1, 0, 0, 0, 171, 172, 5, 45, 0, 0, 172, 174, 3, 100, 50, 0, 173, 175, 5, 2, 0,
        0, 174, 173, 1, 0, 0, 0, 174, 175, 1, 0, 0, 0, 175, 178, 1, 0, 0, 0, 176, 179, 3, 86, 43,
        0, 177, 179, 3, 42, 21, 0, 178, 176, 1, 0, 0, 0, 178, 177, 1, 0, 0, 0, 179, 180, 1, 0,
        0, 0, 180, 181, 3, 72, 36, 0, 181, 15, 1, 0, 0, 0, 182, 183, 5, 46, 0, 0, 183, 185, 3,
        100, 50, 0, 184, 186, 5, 2, 0, 0, 185, 184, 1, 0, 0, 0, 185, 186, 1, 0, 0, 0, 186, 187,
        1, 0, 0, 0, 187, 188, 3, 52, 26, 0, 188, 189, 3, 72, 36, 0, 189, 17, 1, 0, 0, 0, 190, 192,
        5, 48, 0, 0, 191, 193, 3, 60, 30, 0, 192, 191, 1, 0, 0, 0, 192, 193, 1, 0, 0, 0, 193, 194,
        1, 0, 0, 0, 194, 195, 3, 72, 36, 0, 195, 19, 1, 0, 0, 0, 196, 197, 3, 30, 15, 0, 197, 198,
        3, 60, 30, 0, 198, 199, 3, 72, 36, 0, 199, 21, 1, 0, 0, 0, 200, 204, 3, 48, 24, 0, 201,
        204, 3, 50, 25, 0, 202, 204, 3, 52, 26, 0, 203, 200, 1, 0, 0, 0, 203, 201, 1, 0, 0, 0,
        203, 202, 1, 0, 0, 0, 204, 23, 1, 0, 0, 0, 205, 206, 5, 3, 0, 0, 206, 207, 5, 55, 0, 0,
        207, 208, 5, 4, 0, 0, 208, 209, 5, 55, 0, 0, 209, 210, 5, 5, 0, 0, 210, 25, 1, 0, 0, 0,
        211, 212, 5, 6, 0, 0, 212, 213, 5, 55, 0, 0, 213, 214, 5, 4, 0, 0, 214, 215, 5, 55, 0,
        0, 215, 216, 5, 7, 0, 0, 216, 27, 1, 0, 0, 0, 217, 222, 5, 8, 0, 0, 218, 223, 3, 100, 50,
        0, 219, 223, 3, 54, 27, 0, 220, 223, 3, 24, 12, 0, 221, 223, 3, 26, 13, 0, 222, 218,
        1, 0, 0, 0, 222, 219, 1, 0, 0, 0, 222, 220, 1, 0, 0, 0, 222, 221, 1, 0, 0, 0, 223, 29, 1,
        0, 0, 0, 224, 225, 3, 28, 14, 0, 225, 226, 5, 50, 0, 0, 226, 228, 1, 0, 0, 0, 227, 224,
        1, 0, 0, 0, 228, 231, 1, 0, 0, 0, 229, 227, 1, 0, 0, 0, 229, 230, 1, 0, 0, 0, 230, 31, 1,
        0, 0, 0, 231, 229, 1, 0, 0, 0, 232, 234, 7, 0, 0, 0, 233, 232, 1, 0, 0, 0, 234, 237, 1,
        0, 0, 0, 235, 233, 1, 0, 0, 0, 235, 236, 1, 0, 0, 0, 236, 33, 1, 0, 0, 0, 237, 235, 1, 0,
        0, 0, 238, 240, 5, 14, 0, 0, 239, 241, 3, 74, 37, 0, 240, 239, 1, 0, 0, 0, 240, 241, 1,
        0, 0, 0, 241, 242, 1, 0, 0, 0, 242, 250, 3, 40, 20, 0, 243, 245, 5, 4, 0, 0, 244, 246,
        3, 74, 37, 0, 245, 244, 1, 0, 0, 0, 245, 246, 1, 0, 0, 0, 246, 247, 1, 0, 0, 0, 247, 249,
        3, 40, 20, 0, 248, 243, 1, 0, 0, 0, 249, 252, 1, 0, 0, 0, 250, 248, 1, 0, 0, 0, 250, 251,
        1, 0, 0, 0, 251, 254, 1, 0, 0, 0, 252, 250, 1, 0, 0, 0, 253, 255, 3, 74, 37, 0, 254, 253,
        1, 0, 0, 0, 254, 255, 1, 0, 0, 0, 255, 256, 1, 0, 0, 0, 256, 257, 5, 15, 0, 0, 257, 35,
        1, 0, 0, 0, 258, 260, 5, 14, 0, 0, 259, 261, 3, 74, 37, 0, 260, 259, 1, 0, 0, 0, 260, 261,
        1, 0, 0, 0, 261, 262, 1, 0, 0, 0, 262, 270, 3, 44, 22, 0, 263, 265, 5, 4, 0, 0, 264, 266,
        3, 74, 37, 0, 265, 264, 1, 0, 0, 0, 265, 266, 1, 0, 0, 0, 266, 267, 1, 0, 0, 0, 267, 269,
        3, 44, 22, 0, 268, 263, 1, 0, 0, 0, 269, 272, 1, 0, 0, 0, 270, 268, 1, 0, 0, 0, 270, 271,
        1, 0, 0, 0, 271, 274, 1, 0, 0, 0, 272, 270, 1, 0, 0, 0, 273, 275, 3, 74, 37, 0, 274, 273,
        1, 0, 0, 0, 274, 275, 1, 0, 0, 0, 275, 276, 1, 0, 0, 0, 276, 277, 5, 15, 0, 0, 277, 37,
        1, 0, 0, 0, 278, 280, 5, 3, 0, 0, 279, 281, 3, 74, 37, 0, 280, 279, 1, 0, 0, 0, 280, 281,
        1, 0, 0, 0, 281, 293, 1, 0, 0, 0, 282, 290, 3, 44, 22, 0, 283, 285, 5, 4, 0, 0, 284, 286,
        3, 74, 37, 0, 285, 284, 1, 0, 0, 0, 285, 286, 1, 0, 0, 0, 286, 287, 1, 0, 0, 0, 287, 289,
        3, 44, 22, 0, 288, 283, 1, 0, 0, 0, 289, 292, 1, 0, 0, 0, 290, 288, 1, 0, 0, 0, 290, 291,
        1, 0, 0, 0, 291, 294, 1, 0, 0, 0, 292, 290, 1, 0, 0, 0, 293, 282, 1, 0, 0, 0, 293, 294,
        1, 0, 0, 0, 294, 296, 1, 0, 0, 0, 295, 297, 3, 74, 37, 0, 296, 295, 1, 0, 0, 0, 296, 297,
        1, 0, 0, 0, 297, 298, 1, 0, 0, 0, 298, 299, 5, 5, 0, 0, 299, 39, 1, 0, 0, 0, 300, 303, 3,
        60, 30, 0, 301, 303, 3, 46, 23, 0, 302, 300, 1, 0, 0, 0, 302, 301, 1, 0, 0, 0, 303, 41,
        1, 0, 0, 0, 304, 306, 5, 16, 0, 0, 305, 307, 3, 74, 37, 0, 306, 305, 1, 0, 0, 0, 306, 307,
        1, 0, 0, 0, 307, 319, 1, 0, 0, 0, 308, 316, 3, 44, 22, 0, 309, 311, 5, 4, 0, 0, 310, 312,
        3, 74, 37, 0, 311, 310, 1, 0, 0, 0, 311, 312, 1, 0, 0, 0, 312, 313, 1, 0, 0, 0, 313, 315,
        3, 44, 22, 0, 314, 309, 1, 0, 0, 0, 315, 318, 1, 0, 0, 0, 316, 314, 1, 0, 0, 0, 316, 317,
        1, 0, 0, 0, 317, 320, 1, 0, 0, 0, 318, 316, 1, 0, 0, 0, 319, 308, 1, 0, 0, 0, 319, 320,
        1, 0, 0, 0, 320, 322, 1, 0, 0, 0, 321, 323, 3, 74, 37, 0, 322, 321, 1, 0, 0, 0, 322, 323,
        1, 0, 0, 0, 323, 324, 1, 0, 0, 0, 324, 325, 5, 17, 0, 0, 325, 43, 1, 0, 0, 0, 326, 328,
        3, 100, 50, 0, 327, 329, 3, 28, 14, 0, 328, 327, 1, 0, 0, 0, 328, 329, 1, 0, 0, 0, 329,
        330, 1, 0, 0, 0, 330, 331, 5, 1, 0, 0, 331, 334, 3, 98, 49, 0, 332, 333, 5, 2, 0, 0, 333,
        335, 3, 60, 30, 0, 334, 332, 1, 0, 0, 0, 334, 335, 1, 0, 0, 0, 335, 45, 1, 0, 0, 0, 336,
        337, 3, 100, 50, 0, 337, 338, 5, 2, 0, 0, 338, 339, 3, 60, 30, 0, 339, 47, 1, 0, 0, 0,
        340, 349, 3, 100, 50, 0, 341, 344, 5, 6, 0, 0, 342, 345, 5, 55, 0, 0, 343, 345, 3, 100,
        50, 0, 344, 342, 1, 0, 0, 0, 344, 343, 1, 0, 0, 0, 345, 346, 1, 0, 0, 0, 346, 348, 5, 7,
        0, 0, 347, 341, 1, 0, 0, 0, 348, 351, 1, 0, 0, 0, 349, 347, 1, 0, 0, 0, 349, 350, 1, 0,
        0, 0, 350, 49, 1, 0, 0, 0, 351, 349, 1, 0, 0, 0, 352, 354, 5, 6, 0, 0, 353, 355, 3, 74,
        37, 0, 354, 353, 1, 0, 0, 0, 354, 355, 1, 0, 0, 0, 355, 367, 1, 0, 0, 0, 356, 364, 3, 100,
        50, 0, 357, 359, 5, 4, 0, 0, 358, 360, 3, 74, 37, 0, 359, 358, 1, 0, 0, 0, 359, 360, 1,
        0, 0, 0, 360, 361, 1, 0, 0, 0, 361, 363, 3, 100, 50, 0, 362, 357, 1, 0, 0, 0, 363, 366,
        1, 0, 0, 0, 364, 362, 1, 0, 0, 0, 364, 365, 1, 0, 0, 0, 365, 368, 1, 0, 0, 0, 366, 364,
        1, 0, 0, 0, 367, 356, 1, 0, 0, 0, 367, 368, 1, 0, 0, 0, 368, 370, 1, 0, 0, 0, 369, 371,
        3, 74, 37, 0, 370, 369, 1, 0, 0, 0, 370, 371, 1, 0, 0, 0, 371, 372, 1, 0, 0, 0, 372, 373,
        5, 7, 0, 0, 373, 51, 1, 0, 0, 0, 374, 376, 5, 16, 0, 0, 375, 377, 3, 74, 37, 0, 376, 375,
        1, 0, 0, 0, 376, 377, 1, 0, 0, 0, 377, 389, 1, 0, 0, 0, 378, 386, 3, 100, 50, 0, 379, 381,
        5, 4, 0, 0, 380, 382, 3, 74, 37, 0, 381, 380, 1, 0, 0, 0, 381, 382, 1, 0, 0, 0, 382, 383,
        1, 0, 0, 0, 383, 385, 3, 100, 50, 0, 384, 379, 1, 0, 0, 0, 385, 388, 1, 0, 0, 0, 386, 384,
        1, 0, 0, 0, 386, 387, 1, 0, 0, 0, 387, 390, 1, 0, 0, 0, 388, 386, 1, 0, 0, 0, 389, 378,
        1, 0, 0, 0, 389, 390, 1, 0, 0, 0, 390, 392, 1, 0, 0, 0, 391, 393, 3, 74, 37, 0, 392, 391,
        1, 0, 0, 0, 392, 393, 1, 0, 0, 0, 393, 394, 1, 0, 0, 0, 394, 395, 5, 17, 0, 0, 395, 53,
        1, 0, 0, 0, 396, 398, 5, 16, 0, 0, 397, 399, 3, 74, 37, 0, 398, 397, 1, 0, 0, 0, 398, 399,
        1, 0, 0, 0, 399, 411, 1, 0, 0, 0, 400, 408, 3, 46, 23, 0, 401, 403, 5, 4, 0, 0, 402, 404,
        3, 74, 37, 0, 403, 402, 1, 0, 0, 0, 403, 404, 1, 0, 0, 0, 404, 405, 1, 0, 0, 0, 405, 407,
        3, 46, 23, 0, 406, 401, 1, 0, 0, 0, 407, 410, 1, 0, 0, 0, 408, 406, 1, 0, 0, 0, 408, 409,
        1, 0, 0, 0, 409, 412, 1, 0, 0, 0, 410, 408, 1, 0, 0, 0, 411, 400, 1, 0, 0, 0, 411, 412,
        1, 0, 0, 0, 412, 414, 1, 0, 0, 0, 413, 415, 3, 74, 37, 0, 414, 413, 1, 0, 0, 0, 414, 415,
        1, 0, 0, 0, 415, 416, 1, 0, 0, 0, 416, 417, 5, 17, 0, 0, 417, 55, 1, 0, 0, 0, 418, 420,
        5, 6, 0, 0, 419, 421, 3, 74, 37, 0, 420, 419, 1, 0, 0, 0, 420, 421, 1, 0, 0, 0, 421, 433,
        1, 0, 0, 0, 422, 430, 3, 60, 30, 0, 423, 425, 5, 4, 0, 0, 424, 426, 3, 74, 37, 0, 425,
        424, 1, 0, 0, 0, 425, 426, 1, 0, 0, 0, 426, 427, 1, 0, 0, 0, 427, 429, 3, 60, 30, 0, 428,
        423, 1, 0, 0, 0, 429, 432, 1, 0, 0, 0, 430, 428, 1, 0, 0, 0, 430, 431, 1, 0, 0, 0, 431,
        434, 1, 0, 0, 0, 432, 430, 1, 0, 0, 0, 433, 422, 1, 0, 0, 0, 433, 434, 1, 0, 0, 0, 434,
        436, 1, 0, 0, 0, 435, 437, 3, 74, 37, 0, 436, 435, 1, 0, 0, 0, 436, 437, 1, 0, 0, 0, 437,
        438, 1, 0, 0, 0, 438, 439, 5, 7, 0, 0, 439, 57, 1, 0, 0, 0, 440, 442, 5, 16, 0, 0, 441,
        443, 3, 2, 1, 0, 442, 441, 1, 0, 0, 0, 442, 443, 1, 0, 0, 0, 443, 445, 1, 0, 0, 0, 444,
        446, 3, 74, 37, 0, 445, 444, 1, 0, 0, 0, 445, 446, 1, 0, 0, 0, 446, 447, 1, 0, 0, 0, 447,
        448, 5, 17, 0, 0, 448, 59, 1, 0, 0, 0, 449, 452, 3, 62, 31, 0, 450, 451, 5, 18, 0, 0, 451,
        453, 3, 86, 43, 0, 452, 450, 1, 0, 0, 0, 452, 453, 1, 0, 0, 0, 453, 61, 1, 0, 0, 0, 454,
        456, 3, 64, 32, 0, 455, 454, 1, 0, 0, 0, 456, 457, 1, 0, 0, 0, 457, 455, 1, 0, 0, 0, 457,
        458, 1, 0, 0, 0, 458, 63, 1, 0, 0, 0, 459, 462, 3, 66, 33, 0, 460, 462, 3, 68, 34, 0, 461,
        459, 1, 0, 0, 0, 461, 460, 1, 0, 0, 0, 462, 65, 1, 0, 0, 0, 463, 469, 3, 48, 24, 0, 464,
        469, 3, 70, 35, 0, 465, 469, 3, 78, 39, 0, 466, 469, 3, 56, 28, 0, 467, 469, 3, 54, 27,
        0, 468, 463, 1, 0, 0, 0, 468, 464, 1, 0, 0, 0, 468, 465, 1, 0, 0, 0, 468, 466, 1, 0, 0,
        0, 468, 467, 1, 0, 0, 0, 469, 471, 1, 0, 0, 0, 470, 472, 3, 28, 14, 0, 471, 470, 1, 0,
        0, 0, 471, 472, 1, 0, 0, 0, 472, 67, 1, 0, 0, 0, 473, 474, 6, 34, -1, 0, 474, 475, 3, 70,
        35, 0, 475, 476, 3, 76, 38, 0, 476, 479, 1, 0, 0, 0, 477, 479, 3, 66, 33, 0, 478, 473,
        1, 0, 0, 0, 478, 477, 1, 0, 0, 0, 479, 485, 1, 0, 0, 0, 480, 481, 10, 3, 0, 0, 481, 482,
        5, 19, 0, 0, 482, 484, 3, 66, 33, 0, 483, 480, 1, 0, 0, 0, 484, 487, 1, 0, 0, 0, 485, 483,
        1, 0, 0, 0, 485, 486, 1, 0, 0, 0, 486, 69, 1, 0, 0, 0, 487, 485, 1, 0, 0, 0, 488, 490, 3,
        100, 50, 0, 489, 491, 3, 34, 17, 0, 490, 489, 1, 0, 0, 0, 490, 491, 1, 0, 0, 0, 491, 71,
        1, 0, 0, 0, 492, 496, 3, 74, 37, 0, 493, 496, 5, 20, 0, 0, 494, 496, 5, 0, 0, 1, 495, 492,
        1, 0, 0, 0, 495, 493, 1, 0, 0, 0, 495, 494, 1, 0, 0, 0, 496, 73, 1, 0, 0, 0, 497, 499, 5,
        50, 0, 0, 498, 497, 1, 0, 0, 0, 499, 500, 1, 0, 0, 0, 500, 498, 1, 0, 0, 0, 500, 501, 1,
        0, 0, 0, 501, 75, 1, 0, 0, 0, 502, 504, 5, 3, 0, 0, 503, 505, 3, 74, 37, 0, 504, 503, 1,
        0, 0, 0, 504, 505, 1, 0, 0, 0, 505, 517, 1, 0, 0, 0, 506, 514, 3, 40, 20, 0, 507, 509,
        5, 4, 0, 0, 508, 510, 3, 74, 37, 0, 509, 508, 1, 0, 0, 0, 509, 510, 1, 0, 0, 0, 510, 511,
        1, 0, 0, 0, 511, 513, 3, 40, 20, 0, 512, 507, 1, 0, 0, 0, 513, 516, 1, 0, 0, 0, 514, 512,
        1, 0, 0, 0, 514, 515, 1, 0, 0, 0, 515, 518, 1, 0, 0, 0, 516, 514, 1, 0, 0, 0, 517, 506,
        1, 0, 0, 0, 517, 518, 1, 0, 0, 0, 518, 520, 1, 0, 0, 0, 519, 521, 3, 74, 37, 0, 520, 519,
        1, 0, 0, 0, 520, 521, 1, 0, 0, 0, 521, 522, 1, 0, 0, 0, 522, 523, 5, 5, 0, 0, 523, 77, 1,
        0, 0, 0, 524, 532, 3, 80, 40, 0, 525, 532, 5, 54, 0, 0, 526, 532, 5, 51, 0, 0, 527, 532,
        3, 82, 41, 0, 528, 532, 5, 21, 0, 0, 529, 532, 5, 22, 0, 0, 530, 532, 5, 23, 0, 0, 531,
        524, 1, 0, 0, 0, 531, 525, 1, 0, 0, 0, 531, 526, 1, 0, 0, 0, 531, 527, 1, 0, 0, 0, 531,
        528, 1, 0, 0, 0, 531, 529, 1, 0, 0, 0, 531, 530, 1, 0, 0, 0, 532, 79, 1, 0, 0, 0, 533, 537,
        5, 55, 0, 0, 534, 537, 5, 56, 0, 0, 535, 537, 3, 84, 42, 0, 536, 533, 1, 0, 0, 0, 536,
        534, 1, 0, 0, 0, 536, 535, 1, 0, 0, 0, 537, 539, 1, 0, 0, 0, 538, 540, 5, 53, 0, 0, 539,
        538, 1, 0, 0, 0, 539, 540, 1, 0, 0, 0, 540, 81, 1, 0, 0, 0, 541, 542, 5, 24, 0, 0, 542,
        543, 5, 54, 0, 0, 543, 83, 1, 0, 0, 0, 544, 545, 5, 55, 0, 0, 545, 546, 7, 1, 0, 0, 546,
        547, 5, 55, 0, 0, 547, 553, 5, 27, 0, 0, 548, 549, 5, 56, 0, 0, 549, 550, 7, 1, 0, 0, 550,
        551, 5, 56, 0, 0, 551, 553, 5, 27, 0, 0, 552, 544, 1, 0, 0, 0, 552, 548, 1, 0, 0, 0, 553,
        85, 1, 0, 0, 0, 554, 558, 3, 88, 44, 0, 555, 558, 3, 100, 50, 0, 556, 558, 5, 28, 0, 0,
        557, 554, 1, 0, 0, 0, 557, 555, 1, 0, 0, 0, 557, 556, 1, 0, 0, 0, 558, 87, 1, 0, 0, 0, 559,
        567, 5, 29, 0, 0, 560, 567, 5, 30, 0, 0, 561, 567, 5, 31, 0, 0, 562, 567, 5, 32, 0, 0,
        563, 567, 5, 33, 0, 0, 564, 567, 3, 90, 45, 0, 565, 567, 3, 96, 48, 0, 566, 559, 1, 0,
        0, 0, 566, 560, 1, 0, 0, 0, 566, 561, 1, 0, 0, 0, 566, 562, 1, 0, 0, 0, 566, 563, 1, 0,
        0, 0, 566, 564, 1, 0, 0, 0, 566, 565, 1, 0, 0, 0, 567, 89, 1, 0, 0, 0, 568, 571, 3, 92,
        46, 0, 569, 571, 3, 94, 47, 0, 570, 568, 1, 0, 0, 0, 570, 569, 1, 0, 0, 0, 571, 91, 1,
        0, 0, 0, 572, 573, 7, 2, 0, 0, 573, 93, 1, 0, 0, 0, 574, 579, 5, 37, 0, 0, 575, 576, 5,
        14, 0, 0, 576, 577, 3, 92, 46, 0, 577, 578, 5, 15, 0, 0, 578, 580, 1, 0, 0, 0, 579, 575,
        1, 0, 0, 0, 579, 580, 1, 0, 0, 0, 580, 584, 1, 0, 0, 0, 581, 582, 5, 6, 0, 0, 582, 583,
        5, 55, 0, 0, 583, 585, 5, 7, 0, 0, 584, 581, 1, 0, 0, 0, 584, 585, 1, 0, 0, 0, 585, 602,
        1, 0, 0, 0, 586, 591, 5, 38, 0, 0, 587, 588, 5, 14, 0, 0, 588, 589, 3, 92, 46, 0, 589,
        590, 5, 15, 0, 0, 590, 592, 1, 0, 0, 0, 591, 587, 1, 0, 0, 0, 591, 592, 1, 0, 0, 0, 592,
        598, 1, 0, 0, 0, 593, 594, 5, 6, 0, 0, 594, 595, 5, 55, 0, 0, 595, 597, 5, 7, 0, 0, 596,
        593, 1, 0, 0, 0, 597, 600, 1, 0, 0, 0, 598, 596, 1, 0, 0, 0, 598, 599, 1, 0, 0, 0, 599,
        602, 1, 0, 0, 0, 600, 598, 1, 0, 0, 0, 601, 574, 1, 0, 0, 0, 601, 586, 1, 0, 0, 0, 602,
        95, 1, 0, 0, 0, 603, 615, 5, 39, 0, 0, 604, 605, 5, 14, 0, 0, 605, 610, 3, 98, 49, 0, 606,
        607, 5, 4, 0, 0, 607, 609, 3, 98, 49, 0, 608, 606, 1, 0, 0, 0, 609, 612, 1, 0, 0, 0, 610,
        608, 1, 0, 0, 0, 610, 611, 1, 0, 0, 0, 611, 613, 1, 0, 0, 0, 612, 610, 1, 0, 0, 0, 613,
        614, 5, 15, 0, 0, 614, 616, 1, 0, 0, 0, 615, 604, 1, 0, 0, 0, 615, 616, 1, 0, 0, 0, 616,
        620, 1, 0, 0, 0, 617, 618, 5, 6, 0, 0, 618, 619, 5, 55, 0, 0, 619, 621, 5, 7, 0, 0, 620,
        617, 1, 0, 0, 0, 620, 621, 1, 0, 0, 0, 621, 632, 1, 0, 0, 0, 622, 629, 5, 40, 0, 0, 623,
        624, 5, 14, 0, 0, 624, 625, 3, 86, 43, 0, 625, 626, 5, 4, 0, 0, 626, 627, 3, 98, 49, 0,
        627, 628, 5, 15, 0, 0, 628, 630, 1, 0, 0, 0, 629, 623, 1, 0, 0, 0, 629, 630, 1, 0, 0, 0,
        630, 632, 1, 0, 0, 0, 631, 603, 1, 0, 0, 0, 631, 622, 1, 0, 0, 0, 632, 97, 1, 0, 0, 0, 633,
        635, 3, 86, 43, 0, 634, 636, 5, 41, 0, 0, 635, 634, 1, 0, 0, 0, 635, 636, 1, 0, 0, 0, 636,
        99, 1, 0, 0, 0, 637, 638, 5, 52, 0, 0, 638, 101, 1, 0, 0, 0, 99, 103, 106, 111, 120, 126,
        129, 137, 145, 148, 152, 160, 163, 166, 174, 178, 185, 192, 203, 222, 229, 235,
        240, 245, 250, 254, 260, 265, 270, 274, 280, 285, 290, 293, 296, 302, 306, 311,
        316, 319, 322, 328, 334, 344, 349, 354, 359, 364, 367, 370, 376, 381, 386, 389,
        392, 398, 403, 408, 411, 414, 420, 425, 430, 433, 436, 442, 445, 452, 457, 461,
        468, 471, 478, 485, 490, 495, 500, 504, 509, 514, 517, 520, 531, 536, 539, 552,
        557, 566, 570, 579, 584, 591, 598, 601, 610, 615, 620, 629, 631, 635
    ]


class PslParser(Parser):
    grammarFileName = "Psl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "':'", "'='", "'('", "','", "')'", "'['",
                    "']'", "'@'", "'inner'", "'sync'", "'scoped'", "'static'",
                    "'atomic'", "'<'", "'>'", "'{'", "'}'", "'as'", "'->'",
                    "';'", "'null'", "'true'", "'false'", "'f'", "'+'",
                    "'-'", "'i'", "'any'", "'number'", "'string'", "'bool'",
                    "'functor'", "'block'", "'int'", "'real'", "'complex'",
                    "'array'", "'matrix'", "'list'", "'dict'", "'?'", "'let'",
                    "'use'", "'func'", "'type'", "'enum'", "'with'", "'return'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "LET", "USE", "FUNC", "TYPE",
                     "ENUM", "WITH", "RETURN", "SKIP_", "LINE_END", "MULTI_STR",
                     "IDENTIFIER", "UNIT", "STRING", "INTEGER", "REAL",
                     "DECIMAL_INTEGER"]

    RULE_program = 0
    RULE_stmtList = 1
    RULE_stmt = 2
    RULE_letStmt = 3
    RULE_useStmt = 4
    RULE_withDef = 5
    RULE_funcDef = 6
    RULE_typeDef = 7
    RULE_enumDef = 8
    RULE_retStmt = 9
    RULE_exprStmt = 10
    RULE_carrier = 11
    RULE_biasAnno = 12
    RULE_sizeAnno = 13
    RULE_annotation = 14
    RULE_annotations = 15
    RULE_modifiers = 16
    RULE_withList = 17
    RULE_withDecl = 18
    RULE_paramDef = 19
    RULE_argument = 20
    RULE_typePack = 21
    RULE_keyValDecl = 22
    RULE_keyValExpr = 23
    RULE_entityRef = 24
    RULE_listUnpack = 25
    RULE_dictUnpack = 26
    RULE_dictPack = 27
    RULE_listPack = 28
    RULE_stmtPack = 29
    RULE_entityExpr = 30
    RULE_entityChain = 31
    RULE_chainUnit = 32
    RULE_entity = 33
    RULE_linkCall = 34
    RULE_functorRef = 35
    RULE_stmtEnd = 36
    RULE_sepMark = 37
    RULE_argsList = 38
    RULE_literal = 39
    RULE_value = 40
    RULE_formatStr = 41
    RULE_complex = 42
    RULE_type = 43
    RULE_innerType = 44
    RULE_numberType = 45
    RULE_scalarType = 46
    RULE_vectorType = 47
    RULE_structType = 48
    RULE_nullableType = 49
    RULE_identRef = 50

    ruleNames = ["program", "stmtList", "stmt", "letStmt", "useStmt",
                 "withDef", "funcDef", "typeDef", "enumDef", "retStmt",
                 "exprStmt", "carrier", "biasAnno", "sizeAnno", "annotation",
                 "annotations", "modifiers", "withList", "withDecl", "paramDef",
                 "argument", "typePack", "keyValDecl", "keyValExpr", "entityRef",
                 "listUnpack", "dictUnpack", "dictPack", "listPack", "stmtPack",
                 "entityExpr", "entityChain", "chainUnit", "entity", "linkCall",
                 "functorRef", "stmtEnd", "sepMark", "argsList", "literal",
                 "value", "formatStr", "complex", "type", "innerType",
                 "numberType", "scalarType", "vectorType", "structType",
                 "nullableType", "identRef"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    LET = 42
    USE = 43
    FUNC = 44
    TYPE = 45
    ENUM = 46
    WITH = 47
    RETURN = 48
    SKIP_ = 49
    LINE_END = 50
    MULTI_STR = 51
    IDENTIFIER = 52
    UNIT = 53
    STRING = 54
    INTEGER = 55
    REAL = 56
    DECIMAL_INTEGER = 57

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtList(self):
            return self.getTypedRuleContext(PslParser.StmtListContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_program

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProgram"):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)

    def program(self):

        localctx = PslParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 134540640852721472) != 0):
                self.state = 102
                self.stmtList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.StmtContext)
            else:
                return self.getTypedRuleContext(PslParser.StmtContext, i)

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_stmtList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmtList"):
                listener.enterStmtList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmtList"):
                listener.exitStmtList(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmtList"):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)

    def stmtList(self):

        localctx = PslParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmtList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 105
                        self.sepMark()

                    self.state = 108
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letStmt(self):
            return self.getTypedRuleContext(PslParser.LetStmtContext, 0)

        def useStmt(self):
            return self.getTypedRuleContext(PslParser.UseStmtContext, 0)

        def funcDef(self):
            return self.getTypedRuleContext(PslParser.FuncDefContext, 0)

        def typeDef(self):
            return self.getTypedRuleContext(PslParser.TypeDefContext, 0)

        def enumDef(self):
            return self.getTypedRuleContext(PslParser.EnumDefContext, 0)

        def retStmt(self):
            return self.getTypedRuleContext(PslParser.RetStmtContext, 0)

        def exprStmt(self):
            return self.getTypedRuleContext(PslParser.ExprStmtContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt"):
                listener.enterStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt"):
                listener.exitStmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmt"):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)

    def stmt(self):

        localctx = PslParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.letStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.useStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.funcDef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.typeDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                self.enumDef()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 118
                self.retStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 119
                self.exprStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(PslParser.LET, 0)

        def carrier(self):
            return self.getTypedRuleContext(PslParser.CarrierContext, 0)

        def entityExpr(self):
            return self.getTypedRuleContext(PslParser.EntityExprContext, 0)

        def stmtEnd(self):
            return self.getTypedRuleContext(PslParser.StmtEndContext, 0)

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_letStmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLetStmt"):
                listener.enterLetStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLetStmt"):
                listener.exitLetStmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLetStmt"):
                return visitor.visitLetStmt(self)
            else:
                return visitor.visitChildren(self)

    def letStmt(self):

        localctx = PslParser.LetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_letStmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(PslParser.LET)
            self.state = 123
            self.carrier()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 1:
                self.state = 124
                self.match(PslParser.T__0)
                self.state = 125
                self.type_()

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 128
                self.match(PslParser.T__1)

            self.state = 131
            self.entityExpr()
            self.state = 132
            self.stmtEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(PslParser.USE, 0)

        def carrier(self):
            return self.getTypedRuleContext(PslParser.CarrierContext, 0)

        def entityExpr(self):
            return self.getTypedRuleContext(PslParser.EntityExprContext, 0)

        def stmtEnd(self):
            return self.getTypedRuleContext(PslParser.StmtEndContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_useStmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUseStmt"):
                listener.enterUseStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUseStmt"):
                listener.exitUseStmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitUseStmt"):
                return visitor.visitUseStmt(self)
            else:
                return visitor.visitChildren(self)

    def useStmt(self):

        localctx = PslParser.UseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_useStmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(PslParser.USE)
            self.state = 135
            self.carrier()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 136
                self.match(PslParser.T__1)

            self.state = 139
            self.entityExpr()
            self.state = 140
            self.stmtEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(PslParser.WITH, 0)

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def withDecl(self):
            return self.getTypedRuleContext(PslParser.WithDeclContext, 0)

        def LINE_END(self):
            return self.getToken(PslParser.LINE_END, 0)

        def getRuleIndex(self):
            return PslParser.RULE_withDef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWithDef"):
                listener.enterWithDef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWithDef"):
                listener.exitWithDef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitWithDef"):
                return visitor.visitWithDef(self)
            else:
                return visitor.visitChildren(self)

    def withDef(self):

        localctx = PslParser.WithDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_withDef)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(PslParser.WITH)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.state = 143
                self.identRef()
                pass
            elif token in [14]:
                self.state = 144
                self.withDecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 147
                self.match(PslParser.LINE_END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotations(self):
            return self.getTypedRuleContext(PslParser.AnnotationsContext, 0)

        def modifiers(self):
            return self.getTypedRuleContext(PslParser.ModifiersContext, 0)

        def FUNC(self):
            return self.getToken(PslParser.FUNC, 0)

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def paramDef(self):
            return self.getTypedRuleContext(PslParser.ParamDefContext, 0)

        def stmtPack(self):
            return self.getTypedRuleContext(PslParser.StmtPackContext, 0)

        def stmtEnd(self):
            return self.getTypedRuleContext(PslParser.StmtEndContext, 0)

        def withDef(self):
            return self.getTypedRuleContext(PslParser.WithDefContext, 0)

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def LINE_END(self):
            return self.getToken(PslParser.LINE_END, 0)

        def getRuleIndex(self):
            return PslParser.RULE_funcDef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFuncDef"):
                listener.enterFuncDef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFuncDef"):
                listener.exitFuncDef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFuncDef"):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)

    def funcDef(self):

        localctx = PslParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDef)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.annotations()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 151
                self.withDef()

            self.state = 154
            self.modifiers()
            self.state = 155
            self.match(PslParser.FUNC)
            self.state = 156
            self.identRef()
            self.state = 157
            self.paramDef()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 1:
                self.state = 158
                self.match(PslParser.T__0)
                self.state = 159
                self.type_()

            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 162
                self.match(PslParser.T__1)

            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 165
                self.match(PslParser.LINE_END)

            self.state = 168
            self.stmtPack()
            self.state = 169
            self.stmtEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(PslParser.TYPE, 0)

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def stmtEnd(self):
            return self.getTypedRuleContext(PslParser.StmtEndContext, 0)

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def typePack(self):
            return self.getTypedRuleContext(PslParser.TypePackContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_typeDef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTypeDef"):
                listener.enterTypeDef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTypeDef"):
                listener.exitTypeDef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTypeDef"):
                return visitor.visitTypeDef(self)
            else:
                return visitor.visitChildren(self)

    def typeDef(self):

        localctx = PslParser.TypeDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeDef)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(PslParser.TYPE)
            self.state = 172
            self.identRef()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 173
                self.match(PslParser.T__1)

            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 52]:
                self.state = 176
                self.type_()
                pass
            elif token in [16]:
                self.state = 177
                self.typePack()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 180
            self.stmtEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(PslParser.ENUM, 0)

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def dictUnpack(self):
            return self.getTypedRuleContext(PslParser.DictUnpackContext, 0)

        def stmtEnd(self):
            return self.getTypedRuleContext(PslParser.StmtEndContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_enumDef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEnumDef"):
                listener.enterEnumDef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEnumDef"):
                listener.exitEnumDef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEnumDef"):
                return visitor.visitEnumDef(self)
            else:
                return visitor.visitChildren(self)

    def enumDef(self):

        localctx = PslParser.EnumDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_enumDef)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(PslParser.ENUM)
            self.state = 183
            self.identRef()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 184
                self.match(PslParser.T__1)

            self.state = 187
            self.dictUnpack()
            self.state = 188
            self.stmtEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(PslParser.RETURN, 0)

        def stmtEnd(self):
            return self.getTypedRuleContext(PslParser.StmtEndContext, 0)

        def entityExpr(self):
            return self.getTypedRuleContext(PslParser.EntityExprContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_retStmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRetStmt"):
                listener.enterRetStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRetStmt"):
                listener.exitRetStmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRetStmt"):
                return visitor.visitRetStmt(self)
            else:
                return visitor.visitChildren(self)

    def retStmt(self):

        localctx = PslParser.RetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_retStmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(PslParser.RETURN)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132856189038952512) != 0):
                self.state = 191
                self.entityExpr()

            self.state = 194
            self.stmtEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotations(self):
            return self.getTypedRuleContext(PslParser.AnnotationsContext, 0)

        def entityExpr(self):
            return self.getTypedRuleContext(PslParser.EntityExprContext, 0)

        def stmtEnd(self):
            return self.getTypedRuleContext(PslParser.StmtEndContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_exprStmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExprStmt"):
                listener.enterExprStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExprStmt"):
                listener.exitExprStmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExprStmt"):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)

    def exprStmt(self):

        localctx = PslParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.annotations()
            self.state = 197
            self.entityExpr()
            self.state = 198
            self.stmtEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CarrierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityRef(self):
            return self.getTypedRuleContext(PslParser.EntityRefContext, 0)

        def listUnpack(self):
            return self.getTypedRuleContext(PslParser.ListUnpackContext, 0)

        def dictUnpack(self):
            return self.getTypedRuleContext(PslParser.DictUnpackContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_carrier

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCarrier"):
                listener.enterCarrier(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCarrier"):
                listener.exitCarrier(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCarrier"):
                return visitor.visitCarrier(self)
            else:
                return visitor.visitChildren(self)

    def carrier(self):

        localctx = PslParser.CarrierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_carrier)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.entityRef()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.listUnpack()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.dictUnpack()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BiasAnnoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.INTEGER)
            else:
                return self.getToken(PslParser.INTEGER, i)

        def getRuleIndex(self):
            return PslParser.RULE_biasAnno

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBiasAnno"):
                listener.enterBiasAnno(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBiasAnno"):
                listener.exitBiasAnno(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBiasAnno"):
                return visitor.visitBiasAnno(self)
            else:
                return visitor.visitChildren(self)

    def biasAnno(self):

        localctx = PslParser.BiasAnnoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_biasAnno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(PslParser.T__2)
            self.state = 206
            self.match(PslParser.INTEGER)
            self.state = 207
            self.match(PslParser.T__3)
            self.state = 208
            self.match(PslParser.INTEGER)
            self.state = 209
            self.match(PslParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SizeAnnoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.INTEGER)
            else:
                return self.getToken(PslParser.INTEGER, i)

        def getRuleIndex(self):
            return PslParser.RULE_sizeAnno

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSizeAnno"):
                listener.enterSizeAnno(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSizeAnno"):
                listener.exitSizeAnno(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSizeAnno"):
                return visitor.visitSizeAnno(self)
            else:
                return visitor.visitChildren(self)

    def sizeAnno(self):

        localctx = PslParser.SizeAnnoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sizeAnno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(PslParser.T__5)
            self.state = 212
            self.match(PslParser.INTEGER)
            self.state = 213
            self.match(PslParser.T__3)
            self.state = 214
            self.match(PslParser.INTEGER)
            self.state = 215
            self.match(PslParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def dictPack(self):
            return self.getTypedRuleContext(PslParser.DictPackContext, 0)

        def biasAnno(self):
            return self.getTypedRuleContext(PslParser.BiasAnnoContext, 0)

        def sizeAnno(self):
            return self.getTypedRuleContext(PslParser.SizeAnnoContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_annotation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAnnotation"):
                listener.enterAnnotation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAnnotation"):
                listener.exitAnnotation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAnnotation"):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)

    def annotation(self):

        localctx = PslParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(PslParser.T__7)
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.state = 218
                self.identRef()
                pass
            elif token in [16]:
                self.state = 219
                self.dictPack()
                pass
            elif token in [3]:
                self.state = 220
                self.biasAnno()
                pass
            elif token in [6]:
                self.state = 221
                self.sizeAnno()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnnotationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(PslParser.AnnotationContext, i)

        def LINE_END(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.LINE_END)
            else:
                return self.getToken(PslParser.LINE_END, i)

        def getRuleIndex(self):
            return PslParser.RULE_annotations

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAnnotations"):
                listener.enterAnnotations(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAnnotations"):
                listener.exitAnnotations(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAnnotations"):
                return visitor.visitAnnotations(self)
            else:
                return visitor.visitChildren(self)

    def annotations(self):

        localctx = PslParser.AnnotationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_annotations)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 8:
                self.state = 224
                self.annotation()
                self.state = 225
                self.match(PslParser.LINE_END)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return PslParser.RULE_modifiers

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterModifiers"):
                listener.enterModifiers(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitModifiers"):
                listener.exitModifiers(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitModifiers"):
                return visitor.visitModifiers(self)
            else:
                return visitor.visitChildren(self)

    def modifiers(self):

        localctx = PslParser.ModifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_modifiers)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0):
                self.state = 232
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(PslParser.ArgumentContext, i)

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_withList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWithList"):
                listener.enterWithList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWithList"):
                listener.exitWithList(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitWithList"):
                return visitor.visitWithList(self)
            else:
                return visitor.visitChildren(self)

    def withList(self):

        localctx = PslParser.WithListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_withList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(PslParser.T__13)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 239
                self.sepMark()

            self.state = 242
            self.argument()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 243
                self.match(PslParser.T__3)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 50:
                    self.state = 244
                    self.sepMark()

                self.state = 247
                self.argument()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 253
                self.sepMark()

            self.state = 256
            self.match(PslParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValDecl(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.KeyValDeclContext)
            else:
                return self.getTypedRuleContext(PslParser.KeyValDeclContext, i)

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_withDecl

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWithDecl"):
                listener.enterWithDecl(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWithDecl"):
                listener.exitWithDecl(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitWithDecl"):
                return visitor.visitWithDecl(self)
            else:
                return visitor.visitChildren(self)

    def withDecl(self):

        localctx = PslParser.WithDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_withDecl)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(PslParser.T__13)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 259
                self.sepMark()

            self.state = 262
            self.keyValDecl()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 263
                self.match(PslParser.T__3)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 50:
                    self.state = 264
                    self.sepMark()

                self.state = 267
                self.keyValDecl()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 273
                self.sepMark()

            self.state = 276
            self.match(PslParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def keyValDecl(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.KeyValDeclContext)
            else:
                return self.getTypedRuleContext(PslParser.KeyValDeclContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_paramDef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParamDef"):
                listener.enterParamDef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParamDef"):
                listener.exitParamDef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParamDef"):
                return visitor.visitParamDef(self)
            else:
                return visitor.visitChildren(self)

    def paramDef(self):

        localctx = PslParser.ParamDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramDef)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(PslParser.T__2)
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 29, self._ctx)
            if la_ == 1:
                self.state = 279
                self.sepMark()

            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 282
                self.keyValDecl()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 283
                    self.match(PslParser.T__3)
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 284
                        self.sepMark()

                    self.state = 287
                    self.keyValDecl()
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 295
                self.sepMark()

            self.state = 298
            self.match(PslParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityExpr(self):
            return self.getTypedRuleContext(PslParser.EntityExprContext, 0)

        def keyValExpr(self):
            return self.getTypedRuleContext(PslParser.KeyValExprContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_argument

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArgument"):
                listener.enterArgument(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArgument"):
                listener.exitArgument(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArgument"):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)

    def argument(self):

        localctx = PslParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_argument)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 34, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.entityExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.keyValExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypePackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def keyValDecl(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.KeyValDeclContext)
            else:
                return self.getTypedRuleContext(PslParser.KeyValDeclContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_typePack

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTypePack"):
                listener.enterTypePack(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTypePack"):
                listener.exitTypePack(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTypePack"):
                return visitor.visitTypePack(self)
            else:
                return visitor.visitChildren(self)

    def typePack(self):

        localctx = PslParser.TypePackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typePack)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(PslParser.T__15)
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 35, self._ctx)
            if la_ == 1:
                self.state = 305
                self.sepMark()

            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 308
                self.keyValDecl()
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 309
                    self.match(PslParser.T__3)
                    self.state = 311
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 310
                        self.sepMark()

                    self.state = 313
                    self.keyValDecl()
                    self.state = 318
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 321
                self.sepMark()

            self.state = 324
            self.match(PslParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyValDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def nullableType(self):
            return self.getTypedRuleContext(PslParser.NullableTypeContext, 0)

        def annotation(self):
            return self.getTypedRuleContext(PslParser.AnnotationContext, 0)

        def entityExpr(self):
            return self.getTypedRuleContext(PslParser.EntityExprContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_keyValDecl

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterKeyValDecl"):
                listener.enterKeyValDecl(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitKeyValDecl"):
                listener.exitKeyValDecl(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitKeyValDecl"):
                return visitor.visitKeyValDecl(self)
            else:
                return visitor.visitChildren(self)

    def keyValDecl(self):

        localctx = PslParser.KeyValDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_keyValDecl)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.identRef()
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 8:
                self.state = 327
                self.annotation()

            self.state = 330
            self.match(PslParser.T__0)
            self.state = 331
            self.nullableType()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 332
                self.match(PslParser.T__1)
                self.state = 333
                self.entityExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyValExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def entityExpr(self):
            return self.getTypedRuleContext(PslParser.EntityExprContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_keyValExpr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterKeyValExpr"):
                listener.enterKeyValExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitKeyValExpr"):
                listener.exitKeyValExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitKeyValExpr"):
                return visitor.visitKeyValExpr(self)
            else:
                return visitor.visitChildren(self)

    def keyValExpr(self):

        localctx = PslParser.KeyValExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_keyValExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.identRef()
            self.state = 337
            self.match(PslParser.T__1)
            self.state = 338
            self.entityExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntityRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identRef(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.IdentRefContext)
            else:
                return self.getTypedRuleContext(PslParser.IdentRefContext, i)

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.INTEGER)
            else:
                return self.getToken(PslParser.INTEGER, i)

        def getRuleIndex(self):
            return PslParser.RULE_entityRef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntityRef"):
                listener.enterEntityRef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntityRef"):
                listener.exitEntityRef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEntityRef"):
                return visitor.visitEntityRef(self)
            else:
                return visitor.visitChildren(self)

    def entityRef(self):

        localctx = PslParser.EntityRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_entityRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.identRef()
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 43, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 341
                    self.match(PslParser.T__5)
                    self.state = 344
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [55]:
                        self.state = 342
                        self.match(PslParser.INTEGER)
                        pass
                    elif token in [52]:
                        self.state = 343
                        self.identRef()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 346
                    self.match(PslParser.T__6)
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 43, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListUnpackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def identRef(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.IdentRefContext)
            else:
                return self.getTypedRuleContext(PslParser.IdentRefContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_listUnpack

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterListUnpack"):
                listener.enterListUnpack(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitListUnpack"):
                listener.exitListUnpack(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitListUnpack"):
                return visitor.visitListUnpack(self)
            else:
                return visitor.visitChildren(self)

    def listUnpack(self):

        localctx = PslParser.ListUnpackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_listUnpack)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(PslParser.T__5)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 44, self._ctx)
            if la_ == 1:
                self.state = 353
                self.sepMark()

            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 356
                self.identRef()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 357
                    self.match(PslParser.T__3)
                    self.state = 359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 358
                        self.sepMark()

                    self.state = 361
                    self.identRef()
                    self.state = 366
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 369
                self.sepMark()

            self.state = 372
            self.match(PslParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DictUnpackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def identRef(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.IdentRefContext)
            else:
                return self.getTypedRuleContext(PslParser.IdentRefContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_dictUnpack

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDictUnpack"):
                listener.enterDictUnpack(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDictUnpack"):
                listener.exitDictUnpack(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDictUnpack"):
                return visitor.visitDictUnpack(self)
            else:
                return visitor.visitChildren(self)

    def dictUnpack(self):

        localctx = PslParser.DictUnpackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_dictUnpack)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(PslParser.T__15)
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 49, self._ctx)
            if la_ == 1:
                self.state = 375
                self.sepMark()

            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 378
                self.identRef()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 379
                    self.match(PslParser.T__3)
                    self.state = 381
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 380
                        self.sepMark()

                    self.state = 383
                    self.identRef()
                    self.state = 388
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 391
                self.sepMark()

            self.state = 394
            self.match(PslParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DictPackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def keyValExpr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.KeyValExprContext)
            else:
                return self.getTypedRuleContext(PslParser.KeyValExprContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_dictPack

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDictPack"):
                listener.enterDictPack(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDictPack"):
                listener.exitDictPack(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDictPack"):
                return visitor.visitDictPack(self)
            else:
                return visitor.visitChildren(self)

    def dictPack(self):

        localctx = PslParser.DictPackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dictPack)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(PslParser.T__15)
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 54, self._ctx)
            if la_ == 1:
                self.state = 397
                self.sepMark()

            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 400
                self.keyValExpr()
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 401
                    self.match(PslParser.T__3)
                    self.state = 403
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 402
                        self.sepMark()

                    self.state = 405
                    self.keyValExpr()
                    self.state = 410
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 413
                self.sepMark()

            self.state = 416
            self.match(PslParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListPackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def entityExpr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.EntityExprContext)
            else:
                return self.getTypedRuleContext(PslParser.EntityExprContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_listPack

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterListPack"):
                listener.enterListPack(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitListPack"):
                listener.exitListPack(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitListPack"):
                return visitor.visitListPack(self)
            else:
                return visitor.visitChildren(self)

    def listPack(self):

        localctx = PslParser.ListPackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_listPack)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(PslParser.T__5)
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 59, self._ctx)
            if la_ == 1:
                self.state = 419
                self.sepMark()

            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132856189038952512) != 0):
                self.state = 422
                self.entityExpr()
                self.state = 430
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 423
                    self.match(PslParser.T__3)
                    self.state = 425
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 424
                        self.sepMark()

                    self.state = 427
                    self.entityExpr()
                    self.state = 432
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 435
                self.sepMark()

            self.state = 438
            self.match(PslParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtPackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtList(self):
            return self.getTypedRuleContext(PslParser.StmtListContext, 0)

        def sepMark(self):
            return self.getTypedRuleContext(PslParser.SepMarkContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_stmtPack

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmtPack"):
                listener.enterStmtPack(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmtPack"):
                listener.exitStmtPack(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmtPack"):
                return visitor.visitStmtPack(self)
            else:
                return visitor.visitChildren(self)

    def stmtPack(self):

        localctx = PslParser.StmtPackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmtPack)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(PslParser.T__15)
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 64, self._ctx)
            if la_ == 1:
                self.state = 441
                self.stmtList()

            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 444
                self.sepMark()

            self.state = 447
            self.match(PslParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityChain(self):
            return self.getTypedRuleContext(PslParser.EntityChainContext, 0)

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_entityExpr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntityExpr"):
                listener.enterEntityExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntityExpr"):
                listener.exitEntityExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEntityExpr"):
                return visitor.visitEntityExpr(self)
            else:
                return visitor.visitChildren(self)

    def entityExpr(self):

        localctx = PslParser.EntityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_entityExpr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.entityChain()
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 18:
                self.state = 450
                self.match(PslParser.T__17)
                self.state = 451
                self.type_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntityChainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chainUnit(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.ChainUnitContext)
            else:
                return self.getTypedRuleContext(PslParser.ChainUnitContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_entityChain

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntityChain"):
                listener.enterEntityChain(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntityChain"):
                listener.exitEntityChain(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEntityChain"):
                return visitor.visitEntityChain(self)
            else:
                return visitor.visitChildren(self)

    def entityChain(self):

        localctx = PslParser.EntityChainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_entityChain)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 454
                self.chainUnit()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 132856189038952512) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ChainUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entity(self):
            return self.getTypedRuleContext(PslParser.EntityContext, 0)

        def linkCall(self):
            return self.getTypedRuleContext(PslParser.LinkCallContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_chainUnit

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterChainUnit"):
                listener.enterChainUnit(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitChainUnit"):
                listener.exitChainUnit(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitChainUnit"):
                return visitor.visitChainUnit(self)
            else:
                return visitor.visitChildren(self)

    def chainUnit(self):

        localctx = PslParser.ChainUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_chainUnit)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 68, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.linkCall(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityRef(self):
            return self.getTypedRuleContext(PslParser.EntityRefContext, 0)

        def functorRef(self):
            return self.getTypedRuleContext(PslParser.FunctorRefContext, 0)

        def literal(self):
            return self.getTypedRuleContext(PslParser.LiteralContext, 0)

        def listPack(self):
            return self.getTypedRuleContext(PslParser.ListPackContext, 0)

        def dictPack(self):
            return self.getTypedRuleContext(PslParser.DictPackContext, 0)

        def annotation(self):
            return self.getTypedRuleContext(PslParser.AnnotationContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_entity

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntity"):
                listener.enterEntity(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntity"):
                listener.exitEntity(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEntity"):
                return visitor.visitEntity(self)
            else:
                return visitor.visitChildren(self)

    def entity(self):

        localctx = PslParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_entity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 69, self._ctx)
            if la_ == 1:
                self.state = 463
                self.entityRef()
                pass

            elif la_ == 2:
                self.state = 464
                self.functorRef()
                pass

            elif la_ == 3:
                self.state = 465
                self.literal()
                pass

            elif la_ == 4:
                self.state = 466
                self.listPack()
                pass

            elif la_ == 5:
                self.state = 467
                self.dictPack()
                pass

            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 70, self._ctx)
            if la_ == 1:
                self.state = 470
                self.annotation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LinkCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functorRef(self):
            return self.getTypedRuleContext(PslParser.FunctorRefContext, 0)

        def argsList(self):
            return self.getTypedRuleContext(PslParser.ArgsListContext, 0)

        def entity(self):
            return self.getTypedRuleContext(PslParser.EntityContext, 0)

        def linkCall(self):
            return self.getTypedRuleContext(PslParser.LinkCallContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_linkCall

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLinkCall"):
                listener.enterLinkCall(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLinkCall"):
                listener.exitLinkCall(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLinkCall"):
                return visitor.visitLinkCall(self)
            else:
                return visitor.visitChildren(self)

    def linkCall(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PslParser.LinkCallContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_linkCall, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 71, self._ctx)
            if la_ == 1:
                self.state = 474
                self.functorRef()
                self.state = 475
                self.argsList()
                pass

            elif la_ == 2:
                self.state = 477
                self.entity()
                pass

            self._ctx.stop = self._input.LT(-1)
            self.state = 485
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 72, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PslParser.LinkCallContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_linkCall)
                    self.state = 480
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 481
                    self.match(PslParser.T__18)
                    self.state = 482
                    self.entity()
                self.state = 487
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 72, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FunctorRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def withList(self):
            return self.getTypedRuleContext(PslParser.WithListContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_functorRef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFunctorRef"):
                listener.enterFunctorRef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFunctorRef"):
                listener.exitFunctorRef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFunctorRef"):
                return visitor.visitFunctorRef(self)
            else:
                return visitor.visitChildren(self)

    def functorRef(self):

        localctx = PslParser.FunctorRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_functorRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.identRef()
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 73, self._ctx)
            if la_ == 1:
                self.state = 489
                self.withList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtEndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self):
            return self.getTypedRuleContext(PslParser.SepMarkContext, 0)

        def EOF(self):
            return self.getToken(PslParser.EOF, 0)

        def getRuleIndex(self):
            return PslParser.RULE_stmtEnd

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmtEnd"):
                listener.enterStmtEnd(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmtEnd"):
                listener.exitStmtEnd(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmtEnd"):
                return visitor.visitStmtEnd(self)
            else:
                return visitor.visitChildren(self)

    def stmtEnd(self):

        localctx = PslParser.StmtEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmtEnd)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.sepMark()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.match(PslParser.T__19)
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self.match(PslParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SepMarkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_END(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.LINE_END)
            else:
                return self.getToken(PslParser.LINE_END, i)

        def getRuleIndex(self):
            return PslParser.RULE_sepMark

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSepMark"):
                listener.enterSepMark(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSepMark"):
                listener.exitSepMark(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSepMark"):
                return visitor.visitSepMark(self)
            else:
                return visitor.visitChildren(self)

    def sepMark(self):

        localctx = PslParser.SepMarkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_sepMark)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 497
                    self.match(PslParser.LINE_END)

                else:
                    raise NoViableAltException(self)
                self.state = 500
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 75, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgsListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sepMark(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.SepMarkContext)
            else:
                return self.getTypedRuleContext(PslParser.SepMarkContext, i)

        def argument(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(PslParser.ArgumentContext, i)

        def getRuleIndex(self):
            return PslParser.RULE_argsList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArgsList"):
                listener.enterArgsList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArgsList"):
                listener.exitArgsList(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArgsList"):
                return visitor.visitArgsList(self)
            else:
                return visitor.visitChildren(self)

    def argsList(self):

        localctx = PslParser.ArgsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_argsList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(PslParser.T__2)
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 76, self._ctx)
            if la_ == 1:
                self.state = 503
                self.sepMark()

            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132856189038952512) != 0):
                self.state = 506
                self.argument()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 507
                    self.match(PslParser.T__3)
                    self.state = 509
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 508
                        self.sepMark()

                    self.state = 511
                    self.argument()
                    self.state = 516
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 519
                self.sepMark()

            self.state = 522
            self.match(PslParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PslParser.ValueContext, 0)

        def STRING(self):
            return self.getToken(PslParser.STRING, 0)

        def MULTI_STR(self):
            return self.getToken(PslParser.MULTI_STR, 0)

        def formatStr(self):
            return self.getTypedRuleContext(PslParser.FormatStrContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_literal

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLiteral"):
                listener.enterLiteral(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLiteral"):
                listener.exitLiteral(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLiteral"):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)

    def literal(self):

        localctx = PslParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal)
        try:
            self.state = 531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.value()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.match(PslParser.STRING)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 526
                self.match(PslParser.MULTI_STR)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 527
                self.formatStr()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 528
                self.match(PslParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 529
                self.match(PslParser.T__21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 7)
                self.state = 530
                self.match(PslParser.T__22)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(PslParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(PslParser.REAL, 0)

        def complex_(self):
            return self.getTypedRuleContext(PslParser.ComplexContext, 0)

        def UNIT(self):
            return self.getToken(PslParser.UNIT, 0)

        def getRuleIndex(self):
            return PslParser.RULE_value

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterValue"):
                listener.enterValue(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitValue"):
                listener.exitValue(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitValue"):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)

    def value(self):

        localctx = PslParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 82, self._ctx)
            if la_ == 1:
                self.state = 533
                self.match(PslParser.INTEGER)
                pass

            elif la_ == 2:
                self.state = 534
                self.match(PslParser.REAL)
                pass

            elif la_ == 3:
                self.state = 535
                self.complex_()
                pass

            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 83, self._ctx)
            if la_ == 1:
                self.state = 538
                self.match(PslParser.UNIT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormatStrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PslParser.STRING, 0)

        def getRuleIndex(self):
            return PslParser.RULE_formatStr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFormatStr"):
                listener.enterFormatStr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFormatStr"):
                listener.exitFormatStr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFormatStr"):
                return visitor.visitFormatStr(self)
            else:
                return visitor.visitChildren(self)

    def formatStr(self):

        localctx = PslParser.FormatStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_formatStr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(PslParser.T__23)
            self.state = 542
            self.match(PslParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComplexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.INTEGER)
            else:
                return self.getToken(PslParser.INTEGER, i)

        def REAL(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.REAL)
            else:
                return self.getToken(PslParser.REAL, i)

        def getRuleIndex(self):
            return PslParser.RULE_complex

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterComplex"):
                listener.enterComplex(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitComplex"):
                listener.exitComplex(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitComplex"):
                return visitor.visitComplex(self)
            else:
                return visitor.visitChildren(self)

    def complex_(self):

        localctx = PslParser.ComplexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_complex)
        self._la = 0  # Token type
        try:
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.match(PslParser.INTEGER)
                self.state = 545
                _la = self._input.LA(1)
                if not (_la == 25 or _la == 26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 546
                self.match(PslParser.INTEGER)
                self.state = 547
                self.match(PslParser.T__26)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.match(PslParser.REAL)
                self.state = 549
                _la = self._input.LA(1)
                if not (_la == 25 or _la == 26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 550
                self.match(PslParser.REAL)
                self.state = 551
                self.match(PslParser.T__26)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def innerType(self):
            return self.getTypedRuleContext(PslParser.InnerTypeContext, 0)

        def identRef(self):
            return self.getTypedRuleContext(PslParser.IdentRefContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterType"):
                listener.enterType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitType"):
                listener.exitType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitType"):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)

    def type_(self):

        localctx = PslParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_type)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.innerType()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.identRef()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.match(PslParser.T__27)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InnerTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numberType(self):
            return self.getTypedRuleContext(PslParser.NumberTypeContext, 0)

        def structType(self):
            return self.getTypedRuleContext(PslParser.StructTypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_innerType

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInnerType"):
                listener.enterInnerType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInnerType"):
                listener.exitInnerType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitInnerType"):
                return visitor.visitInnerType(self)
            else:
                return visitor.visitChildren(self)

    def innerType(self):

        localctx = PslParser.InnerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_innerType)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.match(PslParser.T__28)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                self.match(PslParser.T__29)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 561
                self.match(PslParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 562
                self.match(PslParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 563
                self.match(PslParser.T__32)
                pass
            elif token in [34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 6)
                self.state = 564
                self.numberType()
                pass
            elif token in [39, 40]:
                self.enterOuterAlt(localctx, 7)
                self.state = 565
                self.structType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarType(self):
            return self.getTypedRuleContext(PslParser.ScalarTypeContext, 0)

        def vectorType(self):
            return self.getTypedRuleContext(PslParser.VectorTypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_numberType

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNumberType"):
                listener.enterNumberType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNumberType"):
                listener.exitNumberType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNumberType"):
                return visitor.visitNumberType(self)
            else:
                return visitor.visitChildren(self)

    def numberType(self):

        localctx = PslParser.NumberTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_numberType)
        try:
            self.state = 570
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.scalarType()
                pass
            elif token in [37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.vectorType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ScalarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return PslParser.RULE_scalarType

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterScalarType"):
                listener.enterScalarType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitScalarType"):
                listener.exitScalarType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitScalarType"):
                return visitor.visitScalarType(self)
            else:
                return visitor.visitChildren(self)

    def scalarType(self):

        localctx = PslParser.ScalarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_scalarType)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VectorTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarType(self):
            return self.getTypedRuleContext(PslParser.ScalarTypeContext, 0)

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.INTEGER)
            else:
                return self.getToken(PslParser.INTEGER, i)

        def getRuleIndex(self):
            return PslParser.RULE_vectorType

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVectorType"):
                listener.enterVectorType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVectorType"):
                listener.exitVectorType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVectorType"):
                return visitor.visitVectorType(self)
            else:
                return visitor.visitChildren(self)

    def vectorType(self):

        localctx = PslParser.VectorTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_vectorType)
        self._la = 0  # Token type
        try:
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.match(PslParser.T__36)
                self.state = 579
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 14:
                    self.state = 575
                    self.match(PslParser.T__13)
                    self.state = 576
                    self.scalarType()
                    self.state = 577
                    self.match(PslParser.T__14)

                self.state = 584
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 89, self._ctx)
                if la_ == 1:
                    self.state = 581
                    self.match(PslParser.T__5)
                    self.state = 582
                    self.match(PslParser.INTEGER)
                    self.state = 583
                    self.match(PslParser.T__6)

                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.match(PslParser.T__37)
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 14:
                    self.state = 587
                    self.match(PslParser.T__13)
                    self.state = 588
                    self.scalarType()
                    self.state = 589
                    self.match(PslParser.T__14)

                self.state = 598
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 91, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 593
                        self.match(PslParser.T__5)
                        self.state = 594
                        self.match(PslParser.INTEGER)
                        self.state = 595
                        self.match(PslParser.T__6)
                    self.state = 600
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 91, self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullableType(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.NullableTypeContext)
            else:
                return self.getTypedRuleContext(PslParser.NullableTypeContext, i)

        def INTEGER(self):
            return self.getToken(PslParser.INTEGER, 0)

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_structType

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStructType"):
                listener.enterStructType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStructType"):
                listener.exitStructType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStructType"):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)

    def structType(self):

        localctx = PslParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_structType)
        self._la = 0  # Token type
        try:
            self.state = 631
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.match(PslParser.T__38)
                self.state = 615
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 14:
                    self.state = 604
                    self.match(PslParser.T__13)
                    self.state = 605
                    self.nullableType()
                    self.state = 610
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == 4:
                        self.state = 606
                        self.match(PslParser.T__3)
                        self.state = 607
                        self.nullableType()
                        self.state = 612
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 613
                    self.match(PslParser.T__14)

                self.state = 620
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 95, self._ctx)
                if la_ == 1:
                    self.state = 617
                    self.match(PslParser.T__5)
                    self.state = 618
                    self.match(PslParser.INTEGER)
                    self.state = 619
                    self.match(PslParser.T__6)

                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.match(PslParser.T__39)
                self.state = 629
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 14:
                    self.state = 623
                    self.match(PslParser.T__13)
                    self.state = 624
                    self.type_()
                    self.state = 625
                    self.match(PslParser.T__3)
                    self.state = 626
                    self.nullableType()
                    self.state = 627
                    self.match(PslParser.T__14)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NullableTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_nullableType

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNullableType"):
                listener.enterNullableType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNullableType"):
                listener.exitNullableType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNullableType"):
                return visitor.visitNullableType(self)
            else:
                return visitor.visitChildren(self)

    def nullableType(self):

        localctx = PslParser.NullableTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_nullableType)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.type_()
            self.state = 635
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 41:
                self.state = 634
                self.match(PslParser.T__40)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PslParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PslParser.RULE_identRef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdentRef"):
                listener.enterIdentRef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdentRef"):
                listener.exitIdentRef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdentRef"):
                return visitor.visitIdentRef(self)
            else:
                return visitor.visitChildren(self)

    def identRef(self):

        localctx = PslParser.IdentRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_identRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.match(PslParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.linkCall_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def linkCall_sempred(self, localctx: LinkCallContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 3)
