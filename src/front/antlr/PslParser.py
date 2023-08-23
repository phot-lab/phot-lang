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
        4, 1, 57, 634, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 2, 20,
        7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2, 26, 7, 26,
        2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 2, 30, 7, 30, 2, 31, 7, 31, 2, 32, 7, 32, 2, 33,
        7, 33, 2, 34, 7, 34, 2, 35, 7, 35, 2, 36, 7, 36, 2, 37, 7, 37, 2, 38, 7, 38, 2, 39, 7, 39,
        2, 40, 7, 40, 2, 41, 7, 41, 2, 42, 7, 42, 2, 43, 7, 43, 2, 44, 7, 44, 2, 45, 7, 45, 2, 46,
        7, 46, 2, 47, 7, 47, 2, 48, 7, 48, 2, 49, 7, 49, 1, 0, 3, 0, 102, 8, 0, 1, 1, 3, 1, 105, 8,
        1, 1, 1, 4, 1, 108, 8, 1, 11, 1, 12, 1, 109, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2,
        119, 8, 2, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 125, 8, 3, 1, 3, 3, 3, 128, 8, 3, 1, 3, 1, 3, 1, 3,
        1, 4, 1, 4, 1, 4, 3, 4, 136, 8, 4, 1, 4, 1, 4, 1, 4, 1, 5, 1, 5, 1, 5, 3, 5, 144, 8, 5, 1, 5,
        3, 5, 147, 8, 5, 1, 6, 1, 6, 3, 6, 151, 8, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 3, 6, 159,
        8, 6, 1, 6, 3, 6, 162, 8, 6, 1, 6, 3, 6, 165, 8, 6, 1, 6, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 3, 7,
        173, 8, 7, 1, 7, 1, 7, 3, 7, 177, 8, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 3, 8, 184, 8, 8, 1, 8,
        1, 8, 1, 8, 1, 9, 1, 9, 3, 9, 191, 8, 9, 1, 9, 1, 9, 1, 10, 1, 10, 1, 10, 1, 10, 1, 11, 1, 11,
        1, 11, 3, 11, 202, 8, 11, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13, 1, 13, 1, 13,
        1, 13, 1, 13, 1, 13, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14, 3, 14, 221, 8, 14, 1, 15, 1, 15,
        1, 15, 5, 15, 226, 8, 15, 10, 15, 12, 15, 229, 9, 15, 1, 16, 5, 16, 232, 8, 16, 10, 16,
        12, 16, 235, 9, 16, 1, 17, 1, 17, 3, 17, 239, 8, 17, 1, 17, 1, 17, 1, 17, 3, 17, 244, 8,
        17, 1, 17, 5, 17, 247, 8, 17, 10, 17, 12, 17, 250, 9, 17, 1, 17, 3, 17, 253, 8, 17, 1,
        17, 1, 17, 1, 18, 1, 18, 3, 18, 259, 8, 18, 1, 18, 1, 18, 1, 18, 3, 18, 264, 8, 18, 1, 18,
        5, 18, 267, 8, 18, 10, 18, 12, 18, 270, 9, 18, 1, 18, 3, 18, 273, 8, 18, 1, 18, 1, 18,
        1, 19, 1, 19, 3, 19, 279, 8, 19, 1, 19, 1, 19, 1, 19, 3, 19, 284, 8, 19, 1, 19, 5, 19, 287,
        8, 19, 10, 19, 12, 19, 290, 9, 19, 3, 19, 292, 8, 19, 1, 19, 3, 19, 295, 8, 19, 1, 19,
        1, 19, 1, 20, 1, 20, 3, 20, 301, 8, 20, 1, 21, 1, 21, 3, 21, 305, 8, 21, 1, 21, 1, 21, 1,
        21, 3, 21, 310, 8, 21, 1, 21, 5, 21, 313, 8, 21, 10, 21, 12, 21, 316, 9, 21, 3, 21, 318,
        8, 21, 1, 21, 3, 21, 321, 8, 21, 1, 21, 1, 21, 1, 22, 1, 22, 3, 22, 327, 8, 22, 1, 22, 1,
        22, 1, 22, 1, 22, 3, 22, 333, 8, 22, 1, 23, 1, 23, 1, 23, 1, 23, 1, 24, 1, 24, 1, 24, 1,
        24, 3, 24, 343, 8, 24, 5, 24, 345, 8, 24, 10, 24, 12, 24, 348, 9, 24, 1, 25, 1, 25, 3,
        25, 352, 8, 25, 1, 25, 1, 25, 1, 25, 3, 25, 357, 8, 25, 1, 25, 5, 25, 360, 8, 25, 10, 25,
        12, 25, 363, 9, 25, 3, 25, 365, 8, 25, 1, 25, 3, 25, 368, 8, 25, 1, 25, 1, 25, 1, 26, 1,
        26, 3, 26, 374, 8, 26, 1, 26, 1, 26, 1, 26, 3, 26, 379, 8, 26, 1, 26, 5, 26, 382, 8, 26,
        10, 26, 12, 26, 385, 9, 26, 3, 26, 387, 8, 26, 1, 26, 3, 26, 390, 8, 26, 1, 26, 1, 26,
        1, 27, 1, 27, 3, 27, 396, 8, 27, 1, 27, 1, 27, 1, 27, 3, 27, 401, 8, 27, 1, 27, 5, 27, 404,
        8, 27, 10, 27, 12, 27, 407, 9, 27, 3, 27, 409, 8, 27, 1, 27, 3, 27, 412, 8, 27, 1, 27,
        1, 27, 1, 28, 1, 28, 3, 28, 418, 8, 28, 1, 28, 1, 28, 1, 28, 3, 28, 423, 8, 28, 1, 28, 5,
        28, 426, 8, 28, 10, 28, 12, 28, 429, 9, 28, 3, 28, 431, 8, 28, 1, 28, 3, 28, 434, 8, 28,
        1, 28, 1, 28, 1, 29, 1, 29, 3, 29, 440, 8, 29, 1, 29, 3, 29, 443, 8, 29, 1, 29, 1, 29, 1,
        30, 1, 30, 1, 30, 3, 30, 450, 8, 30, 1, 31, 4, 31, 453, 8, 31, 11, 31, 12, 31, 454, 1,
        32, 1, 32, 3, 32, 459, 8, 32, 1, 33, 1, 33, 1, 33, 1, 33, 1, 33, 3, 33, 466, 8, 33, 1, 33,
        3, 33, 469, 8, 33, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34, 3, 34, 476, 8, 34, 1, 34, 1, 34, 1,
        34, 5, 34, 481, 8, 34, 10, 34, 12, 34, 484, 9, 34, 1, 35, 1, 35, 3, 35, 488, 8, 35, 1,
        36, 1, 36, 1, 36, 3, 36, 493, 8, 36, 1, 37, 4, 37, 496, 8, 37, 11, 37, 12, 37, 497, 1,
        38, 1, 38, 3, 38, 502, 8, 38, 1, 38, 1, 38, 1, 38, 3, 38, 507, 8, 38, 1, 38, 5, 38, 510,
        8, 38, 10, 38, 12, 38, 513, 9, 38, 3, 38, 515, 8, 38, 1, 38, 3, 38, 518, 8, 38, 1, 38,
        1, 38, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 3, 39, 529, 8, 39, 1, 40, 1, 40,
        1, 40, 3, 40, 534, 8, 40, 1, 40, 3, 40, 537, 8, 40, 1, 41, 1, 41, 1, 41, 3, 41, 542, 8,
        41, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 3, 42, 551, 8, 42, 1, 43, 1, 43, 3,
        43, 555, 8, 43, 1, 44, 1, 44, 1, 45, 1, 45, 1, 45, 1, 45, 1, 45, 1, 45, 1, 45, 1, 45, 3,
        45, 567, 8, 45, 1, 46, 1, 46, 1, 46, 1, 46, 1, 46, 3, 46, 574, 8, 46, 1, 46, 1, 46, 1, 46,
        3, 46, 579, 8, 46, 1, 46, 1, 46, 1, 46, 1, 46, 1, 46, 3, 46, 586, 8, 46, 1, 46, 1, 46, 1,
        46, 5, 46, 591, 8, 46, 10, 46, 12, 46, 594, 9, 46, 3, 46, 596, 8, 46, 1, 47, 1, 47, 1,
        47, 1, 47, 1, 47, 5, 47, 603, 8, 47, 10, 47, 12, 47, 606, 9, 47, 1, 47, 1, 47, 3, 47, 610,
        8, 47, 1, 47, 1, 47, 1, 47, 3, 47, 615, 8, 47, 1, 47, 1, 47, 1, 47, 1, 47, 1, 47, 1, 47,
        1, 47, 3, 47, 624, 8, 47, 3, 47, 626, 8, 47, 1, 48, 1, 48, 3, 48, 630, 8, 48, 1, 49, 1,
        49, 1, 49, 0, 1, 68, 50, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
        34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76,
        78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 0, 3, 1, 0, 28, 32, 1, 0, 42, 44, 1, 0, 16,
        17, 706, 0, 101, 1, 0, 0, 0, 2, 107, 1, 0, 0, 0, 4, 118, 1, 0, 0, 0, 6, 120, 1, 0, 0, 0, 8,
        132, 1, 0, 0, 0, 10, 140, 1, 0, 0, 0, 12, 148, 1, 0, 0, 0, 14, 169, 1, 0, 0, 0, 16, 180,
        1, 0, 0, 0, 18, 188, 1, 0, 0, 0, 20, 194, 1, 0, 0, 0, 22, 201, 1, 0, 0, 0, 24, 203, 1, 0,
        0, 0, 26, 209, 1, 0, 0, 0, 28, 215, 1, 0, 0, 0, 30, 227, 1, 0, 0, 0, 32, 233, 1, 0, 0, 0,
        34, 236, 1, 0, 0, 0, 36, 256, 1, 0, 0, 0, 38, 276, 1, 0, 0, 0, 40, 300, 1, 0, 0, 0, 42, 302,
        1, 0, 0, 0, 44, 324, 1, 0, 0, 0, 46, 334, 1, 0, 0, 0, 48, 338, 1, 0, 0, 0, 50, 349, 1, 0,
        0, 0, 52, 371, 1, 0, 0, 0, 54, 393, 1, 0, 0, 0, 56, 415, 1, 0, 0, 0, 58, 437, 1, 0, 0, 0,
        60, 446, 1, 0, 0, 0, 62, 452, 1, 0, 0, 0, 64, 458, 1, 0, 0, 0, 66, 465, 1, 0, 0, 0, 68, 475,
        1, 0, 0, 0, 70, 485, 1, 0, 0, 0, 72, 492, 1, 0, 0, 0, 74, 495, 1, 0, 0, 0, 76, 499, 1, 0,
        0, 0, 78, 528, 1, 0, 0, 0, 80, 533, 1, 0, 0, 0, 82, 541, 1, 0, 0, 0, 84, 550, 1, 0, 0, 0,
        86, 554, 1, 0, 0, 0, 88, 556, 1, 0, 0, 0, 90, 566, 1, 0, 0, 0, 92, 595, 1, 0, 0, 0, 94, 625,
        1, 0, 0, 0, 96, 627, 1, 0, 0, 0, 98, 631, 1, 0, 0, 0, 100, 102, 3, 2, 1, 0, 101, 100, 1,
        0, 0, 0, 101, 102, 1, 0, 0, 0, 102, 1, 1, 0, 0, 0, 103, 105, 3, 74, 37, 0, 104, 103, 1,
        0, 0, 0, 104, 105, 1, 0, 0, 0, 105, 106, 1, 0, 0, 0, 106, 108, 3, 4, 2, 0, 107, 104, 1,
        0, 0, 0, 108, 109, 1, 0, 0, 0, 109, 107, 1, 0, 0, 0, 109, 110, 1, 0, 0, 0, 110, 3, 1, 0,
        0, 0, 111, 119, 3, 6, 3, 0, 112, 119, 3, 8, 4, 0, 113, 119, 3, 12, 6, 0, 114, 119, 3, 14,
        7, 0, 115, 119, 3, 16, 8, 0, 116, 119, 3, 18, 9, 0, 117, 119, 3, 20, 10, 0, 118, 111,
        1, 0, 0, 0, 118, 112, 1, 0, 0, 0, 118, 113, 1, 0, 0, 0, 118, 114, 1, 0, 0, 0, 118, 115,
        1, 0, 0, 0, 118, 116, 1, 0, 0, 0, 118, 117, 1, 0, 0, 0, 119, 5, 1, 0, 0, 0, 120, 121, 5,
        21, 0, 0, 121, 124, 3, 22, 11, 0, 122, 123, 5, 1, 0, 0, 123, 125, 3, 82, 41, 0, 124, 122,
        1, 0, 0, 0, 124, 125, 1, 0, 0, 0, 125, 127, 1, 0, 0, 0, 126, 128, 5, 2, 0, 0, 127, 126,
        1, 0, 0, 0, 127, 128, 1, 0, 0, 0, 128, 129, 1, 0, 0, 0, 129, 130, 3, 60, 30, 0, 130, 131,
        3, 72, 36, 0, 131, 7, 1, 0, 0, 0, 132, 133, 5, 22, 0, 0, 133, 135, 3, 22, 11, 0, 134, 136,
        5, 2, 0, 0, 135, 134, 1, 0, 0, 0, 135, 136, 1, 0, 0, 0, 136, 137, 1, 0, 0, 0, 137, 138,
        3, 60, 30, 0, 138, 139, 3, 72, 36, 0, 139, 9, 1, 0, 0, 0, 140, 143, 5, 26, 0, 0, 141, 144,
        3, 98, 49, 0, 142, 144, 3, 36, 18, 0, 143, 141, 1, 0, 0, 0, 143, 142, 1, 0, 0, 0, 144,
        146, 1, 0, 0, 0, 145, 147, 5, 50, 0, 0, 146, 145, 1, 0, 0, 0, 146, 147, 1, 0, 0, 0, 147,
        11, 1, 0, 0, 0, 148, 150, 3, 30, 15, 0, 149, 151, 3, 10, 5, 0, 150, 149, 1, 0, 0, 0, 150,
        151, 1, 0, 0, 0, 151, 152, 1, 0, 0, 0, 152, 153, 3, 32, 16, 0, 153, 154, 5, 23, 0, 0, 154,
        155, 3, 98, 49, 0, 155, 158, 3, 38, 19, 0, 156, 157, 5, 1, 0, 0, 157, 159, 3, 82, 41,
        0, 158, 156, 1, 0, 0, 0, 158, 159, 1, 0, 0, 0, 159, 161, 1, 0, 0, 0, 160, 162, 5, 2, 0,
        0, 161, 160, 1, 0, 0, 0, 161, 162, 1, 0, 0, 0, 162, 164, 1, 0, 0, 0, 163, 165, 5, 50, 0,
        0, 164, 163, 1, 0, 0, 0, 164, 165, 1, 0, 0, 0, 165, 166, 1, 0, 0, 0, 166, 167, 3, 58, 29,
        0, 167, 168, 3, 72, 36, 0, 168, 13, 1, 0, 0, 0, 169, 170, 5, 24, 0, 0, 170, 172, 3, 98,
        49, 0, 171, 173, 5, 2, 0, 0, 172, 171, 1, 0, 0, 0, 172, 173, 1, 0, 0, 0, 173, 176, 1, 0,
        0, 0, 174, 177, 3, 82, 41, 0, 175, 177, 3, 42, 21, 0, 176, 174, 1, 0, 0, 0, 176, 175,
        1, 0, 0, 0, 177, 178, 1, 0, 0, 0, 178, 179, 3, 72, 36, 0, 179, 15, 1, 0, 0, 0, 180, 181,
        5, 25, 0, 0, 181, 183, 3, 98, 49, 0, 182, 184, 5, 2, 0, 0, 183, 182, 1, 0, 0, 0, 183, 184,
        1, 0, 0, 0, 184, 185, 1, 0, 0, 0, 185, 186, 3, 52, 26, 0, 186, 187, 3, 72, 36, 0, 187,
        17, 1, 0, 0, 0, 188, 190, 5, 27, 0, 0, 189, 191, 3, 60, 30, 0, 190, 189, 1, 0, 0, 0, 190,
        191, 1, 0, 0, 0, 191, 192, 1, 0, 0, 0, 192, 193, 3, 72, 36, 0, 193, 19, 1, 0, 0, 0, 194,
        195, 3, 30, 15, 0, 195, 196, 3, 60, 30, 0, 196, 197, 3, 72, 36, 0, 197, 21, 1, 0, 0, 0,
        198, 202, 3, 48, 24, 0, 199, 202, 3, 50, 25, 0, 200, 202, 3, 52, 26, 0, 201, 198, 1,
        0, 0, 0, 201, 199, 1, 0, 0, 0, 201, 200, 1, 0, 0, 0, 202, 23, 1, 0, 0, 0, 203, 204, 5, 3,
        0, 0, 204, 205, 5, 56, 0, 0, 205, 206, 5, 4, 0, 0, 206, 207, 5, 56, 0, 0, 207, 208, 5,
        5, 0, 0, 208, 25, 1, 0, 0, 0, 209, 210, 5, 6, 0, 0, 210, 211, 5, 56, 0, 0, 211, 212, 5,
        4, 0, 0, 212, 213, 5, 56, 0, 0, 213, 214, 5, 7, 0, 0, 214, 27, 1, 0, 0, 0, 215, 220, 5,
        8, 0, 0, 216, 221, 3, 98, 49, 0, 217, 221, 3, 54, 27, 0, 218, 221, 3, 24, 12, 0, 219,
        221, 3, 26, 13, 0, 220, 216, 1, 0, 0, 0, 220, 217, 1, 0, 0, 0, 220, 218, 1, 0, 0, 0, 220,
        219, 1, 0, 0, 0, 221, 29, 1, 0, 0, 0, 222, 223, 3, 28, 14, 0, 223, 224, 5, 50, 0, 0, 224,
        226, 1, 0, 0, 0, 225, 222, 1, 0, 0, 0, 226, 229, 1, 0, 0, 0, 227, 225, 1, 0, 0, 0, 227,
        228, 1, 0, 0, 0, 228, 31, 1, 0, 0, 0, 229, 227, 1, 0, 0, 0, 230, 232, 7, 0, 0, 0, 231, 230,
        1, 0, 0, 0, 232, 235, 1, 0, 0, 0, 233, 231, 1, 0, 0, 0, 233, 234, 1, 0, 0, 0, 234, 33, 1,
        0, 0, 0, 235, 233, 1, 0, 0, 0, 236, 238, 5, 9, 0, 0, 237, 239, 3, 74, 37, 0, 238, 237,
        1, 0, 0, 0, 238, 239, 1, 0, 0, 0, 239, 240, 1, 0, 0, 0, 240, 248, 3, 40, 20, 0, 241, 243,
        5, 4, 0, 0, 242, 244, 3, 74, 37, 0, 243, 242, 1, 0, 0, 0, 243, 244, 1, 0, 0, 0, 244, 245,
        1, 0, 0, 0, 245, 247, 3, 40, 20, 0, 246, 241, 1, 0, 0, 0, 247, 250, 1, 0, 0, 0, 248, 246,
        1, 0, 0, 0, 248, 249, 1, 0, 0, 0, 249, 252, 1, 0, 0, 0, 250, 248, 1, 0, 0, 0, 251, 253,
        3, 74, 37, 0, 252, 251, 1, 0, 0, 0, 252, 253, 1, 0, 0, 0, 253, 254, 1, 0, 0, 0, 254, 255,
        5, 10, 0, 0, 255, 35, 1, 0, 0, 0, 256, 258, 5, 9, 0, 0, 257, 259, 3, 74, 37, 0, 258, 257,
        1, 0, 0, 0, 258, 259, 1, 0, 0, 0, 259, 260, 1, 0, 0, 0, 260, 268, 3, 44, 22, 0, 261, 263,
        5, 4, 0, 0, 262, 264, 3, 74, 37, 0, 263, 262, 1, 0, 0, 0, 263, 264, 1, 0, 0, 0, 264, 265,
        1, 0, 0, 0, 265, 267, 3, 44, 22, 0, 266, 261, 1, 0, 0, 0, 267, 270, 1, 0, 0, 0, 268, 266,
        1, 0, 0, 0, 268, 269, 1, 0, 0, 0, 269, 272, 1, 0, 0, 0, 270, 268, 1, 0, 0, 0, 271, 273,
        3, 74, 37, 0, 272, 271, 1, 0, 0, 0, 272, 273, 1, 0, 0, 0, 273, 274, 1, 0, 0, 0, 274, 275,
        5, 10, 0, 0, 275, 37, 1, 0, 0, 0, 276, 278, 5, 3, 0, 0, 277, 279, 3, 74, 37, 0, 278, 277,
        1, 0, 0, 0, 278, 279, 1, 0, 0, 0, 279, 291, 1, 0, 0, 0, 280, 288, 3, 44, 22, 0, 281, 283,
        5, 4, 0, 0, 282, 284, 3, 74, 37, 0, 283, 282, 1, 0, 0, 0, 283, 284, 1, 0, 0, 0, 284, 285,
        1, 0, 0, 0, 285, 287, 3, 44, 22, 0, 286, 281, 1, 0, 0, 0, 287, 290, 1, 0, 0, 0, 288, 286,
        1, 0, 0, 0, 288, 289, 1, 0, 0, 0, 289, 292, 1, 0, 0, 0, 290, 288, 1, 0, 0, 0, 291, 280,
        1, 0, 0, 0, 291, 292, 1, 0, 0, 0, 292, 294, 1, 0, 0, 0, 293, 295, 3, 74, 37, 0, 294, 293,
        1, 0, 0, 0, 294, 295, 1, 0, 0, 0, 295, 296, 1, 0, 0, 0, 296, 297, 5, 5, 0, 0, 297, 39, 1,
        0, 0, 0, 298, 301, 3, 60, 30, 0, 299, 301, 3, 46, 23, 0, 300, 298, 1, 0, 0, 0, 300, 299,
        1, 0, 0, 0, 301, 41, 1, 0, 0, 0, 302, 304, 5, 11, 0, 0, 303, 305, 3, 74, 37, 0, 304, 303,
        1, 0, 0, 0, 304, 305, 1, 0, 0, 0, 305, 317, 1, 0, 0, 0, 306, 314, 3, 44, 22, 0, 307, 309,
        5, 4, 0, 0, 308, 310, 3, 74, 37, 0, 309, 308, 1, 0, 0, 0, 309, 310, 1, 0, 0, 0, 310, 311,
        1, 0, 0, 0, 311, 313, 3, 44, 22, 0, 312, 307, 1, 0, 0, 0, 313, 316, 1, 0, 0, 0, 314, 312,
        1, 0, 0, 0, 314, 315, 1, 0, 0, 0, 315, 318, 1, 0, 0, 0, 316, 314, 1, 0, 0, 0, 317, 306,
        1, 0, 0, 0, 317, 318, 1, 0, 0, 0, 318, 320, 1, 0, 0, 0, 319, 321, 3, 74, 37, 0, 320, 319,
        1, 0, 0, 0, 320, 321, 1, 0, 0, 0, 321, 322, 1, 0, 0, 0, 322, 323, 5, 12, 0, 0, 323, 43,
        1, 0, 0, 0, 324, 326, 3, 98, 49, 0, 325, 327, 3, 28, 14, 0, 326, 325, 1, 0, 0, 0, 326,
        327, 1, 0, 0, 0, 327, 328, 1, 0, 0, 0, 328, 329, 5, 1, 0, 0, 329, 332, 3, 96, 48, 0, 330,
        331, 5, 2, 0, 0, 331, 333, 3, 60, 30, 0, 332, 330, 1, 0, 0, 0, 332, 333, 1, 0, 0, 0, 333,
        45, 1, 0, 0, 0, 334, 335, 3, 98, 49, 0, 335, 336, 5, 2, 0, 0, 336, 337, 3, 60, 30, 0, 337,
        47, 1, 0, 0, 0, 338, 346, 3, 98, 49, 0, 339, 342, 5, 13, 0, 0, 340, 343, 5, 56, 0, 0, 341,
        343, 3, 98, 49, 0, 342, 340, 1, 0, 0, 0, 342, 341, 1, 0, 0, 0, 343, 345, 1, 0, 0, 0, 344,
        339, 1, 0, 0, 0, 345, 348, 1, 0, 0, 0, 346, 344, 1, 0, 0, 0, 346, 347, 1, 0, 0, 0, 347,
        49, 1, 0, 0, 0, 348, 346, 1, 0, 0, 0, 349, 351, 5, 6, 0, 0, 350, 352, 3, 74, 37, 0, 351,
        350, 1, 0, 0, 0, 351, 352, 1, 0, 0, 0, 352, 364, 1, 0, 0, 0, 353, 361, 3, 98, 49, 0, 354,
        356, 5, 4, 0, 0, 355, 357, 3, 74, 37, 0, 356, 355, 1, 0, 0, 0, 356, 357, 1, 0, 0, 0, 357,
        358, 1, 0, 0, 0, 358, 360, 3, 98, 49, 0, 359, 354, 1, 0, 0, 0, 360, 363, 1, 0, 0, 0, 361,
        359, 1, 0, 0, 0, 361, 362, 1, 0, 0, 0, 362, 365, 1, 0, 0, 0, 363, 361, 1, 0, 0, 0, 364,
        353, 1, 0, 0, 0, 364, 365, 1, 0, 0, 0, 365, 367, 1, 0, 0, 0, 366, 368, 3, 74, 37, 0, 367,
        366, 1, 0, 0, 0, 367, 368, 1, 0, 0, 0, 368, 369, 1, 0, 0, 0, 369, 370, 5, 7, 0, 0, 370,
        51, 1, 0, 0, 0, 371, 373, 5, 11, 0, 0, 372, 374, 3, 74, 37, 0, 373, 372, 1, 0, 0, 0, 373,
        374, 1, 0, 0, 0, 374, 386, 1, 0, 0, 0, 375, 383, 3, 98, 49, 0, 376, 378, 5, 4, 0, 0, 377,
        379, 3, 74, 37, 0, 378, 377, 1, 0, 0, 0, 378, 379, 1, 0, 0, 0, 379, 380, 1, 0, 0, 0, 380,
        382, 3, 98, 49, 0, 381, 376, 1, 0, 0, 0, 382, 385, 1, 0, 0, 0, 383, 381, 1, 0, 0, 0, 383,
        384, 1, 0, 0, 0, 384, 387, 1, 0, 0, 0, 385, 383, 1, 0, 0, 0, 386, 375, 1, 0, 0, 0, 386,
        387, 1, 0, 0, 0, 387, 389, 1, 0, 0, 0, 388, 390, 3, 74, 37, 0, 389, 388, 1, 0, 0, 0, 389,
        390, 1, 0, 0, 0, 390, 391, 1, 0, 0, 0, 391, 392, 5, 12, 0, 0, 392, 53, 1, 0, 0, 0, 393,
        395, 5, 11, 0, 0, 394, 396, 3, 74, 37, 0, 395, 394, 1, 0, 0, 0, 395, 396, 1, 0, 0, 0, 396,
        408, 1, 0, 0, 0, 397, 405, 3, 46, 23, 0, 398, 400, 5, 4, 0, 0, 399, 401, 3, 74, 37, 0,
        400, 399, 1, 0, 0, 0, 400, 401, 1, 0, 0, 0, 401, 402, 1, 0, 0, 0, 402, 404, 3, 46, 23,
        0, 403, 398, 1, 0, 0, 0, 404, 407, 1, 0, 0, 0, 405, 403, 1, 0, 0, 0, 405, 406, 1, 0, 0,
        0, 406, 409, 1, 0, 0, 0, 407, 405, 1, 0, 0, 0, 408, 397, 1, 0, 0, 0, 408, 409, 1, 0, 0,
        0, 409, 411, 1, 0, 0, 0, 410, 412, 3, 74, 37, 0, 411, 410, 1, 0, 0, 0, 411, 412, 1, 0,
        0, 0, 412, 413, 1, 0, 0, 0, 413, 414, 5, 12, 0, 0, 414, 55, 1, 0, 0, 0, 415, 417, 5, 6,
        0, 0, 416, 418, 3, 74, 37, 0, 417, 416, 1, 0, 0, 0, 417, 418, 1, 0, 0, 0, 418, 430, 1,
        0, 0, 0, 419, 427, 3, 60, 30, 0, 420, 422, 5, 4, 0, 0, 421, 423, 3, 74, 37, 0, 422, 421,
        1, 0, 0, 0, 422, 423, 1, 0, 0, 0, 423, 424, 1, 0, 0, 0, 424, 426, 3, 60, 30, 0, 425, 420,
        1, 0, 0, 0, 426, 429, 1, 0, 0, 0, 427, 425, 1, 0, 0, 0, 427, 428, 1, 0, 0, 0, 428, 431,
        1, 0, 0, 0, 429, 427, 1, 0, 0, 0, 430, 419, 1, 0, 0, 0, 430, 431, 1, 0, 0, 0, 431, 433,
        1, 0, 0, 0, 432, 434, 3, 74, 37, 0, 433, 432, 1, 0, 0, 0, 433, 434, 1, 0, 0, 0, 434, 435,
        1, 0, 0, 0, 435, 436, 5, 7, 0, 0, 436, 57, 1, 0, 0, 0, 437, 439, 5, 11, 0, 0, 438, 440,
        3, 2, 1, 0, 439, 438, 1, 0, 0, 0, 439, 440, 1, 0, 0, 0, 440, 442, 1, 0, 0, 0, 441, 443,
        3, 74, 37, 0, 442, 441, 1, 0, 0, 0, 442, 443, 1, 0, 0, 0, 443, 444, 1, 0, 0, 0, 444, 445,
        5, 12, 0, 0, 445, 59, 1, 0, 0, 0, 446, 449, 3, 62, 31, 0, 447, 448, 5, 20, 0, 0, 448, 450,
        3, 82, 41, 0, 449, 447, 1, 0, 0, 0, 449, 450, 1, 0, 0, 0, 450, 61, 1, 0, 0, 0, 451, 453,
        3, 64, 32, 0, 452, 451, 1, 0, 0, 0, 453, 454, 1, 0, 0, 0, 454, 452, 1, 0, 0, 0, 454, 455,
        1, 0, 0, 0, 455, 63, 1, 0, 0, 0, 456, 459, 3, 66, 33, 0, 457, 459, 3, 68, 34, 0, 458, 456,
        1, 0, 0, 0, 458, 457, 1, 0, 0, 0, 459, 65, 1, 0, 0, 0, 460, 466, 3, 48, 24, 0, 461, 466,
        3, 70, 35, 0, 462, 466, 3, 78, 39, 0, 463, 466, 3, 56, 28, 0, 464, 466, 3, 54, 27, 0,
        465, 460, 1, 0, 0, 0, 465, 461, 1, 0, 0, 0, 465, 462, 1, 0, 0, 0, 465, 463, 1, 0, 0, 0,
        465, 464, 1, 0, 0, 0, 466, 468, 1, 0, 0, 0, 467, 469, 3, 28, 14, 0, 468, 467, 1, 0, 0,
        0, 468, 469, 1, 0, 0, 0, 469, 67, 1, 0, 0, 0, 470, 471, 6, 34, -1, 0, 471, 472, 3, 70,
        35, 0, 472, 473, 3, 76, 38, 0, 473, 476, 1, 0, 0, 0, 474, 476, 3, 66, 33, 0, 475, 470,
        1, 0, 0, 0, 475, 474, 1, 0, 0, 0, 476, 482, 1, 0, 0, 0, 477, 478, 10, 3, 0, 0, 478, 479,
        5, 14, 0, 0, 479, 481, 3, 66, 33, 0, 480, 477, 1, 0, 0, 0, 481, 484, 1, 0, 0, 0, 482, 480,
        1, 0, 0, 0, 482, 483, 1, 0, 0, 0, 483, 69, 1, 0, 0, 0, 484, 482, 1, 0, 0, 0, 485, 487, 3,
        98, 49, 0, 486, 488, 3, 34, 17, 0, 487, 486, 1, 0, 0, 0, 487, 488, 1, 0, 0, 0, 488, 71,
        1, 0, 0, 0, 489, 493, 3, 74, 37, 0, 490, 493, 5, 15, 0, 0, 491, 493, 5, 0, 0, 1, 492, 489,
        1, 0, 0, 0, 492, 490, 1, 0, 0, 0, 492, 491, 1, 0, 0, 0, 493, 73, 1, 0, 0, 0, 494, 496, 5,
        50, 0, 0, 495, 494, 1, 0, 0, 0, 496, 497, 1, 0, 0, 0, 497, 495, 1, 0, 0, 0, 497, 498, 1,
        0, 0, 0, 498, 75, 1, 0, 0, 0, 499, 501, 5, 3, 0, 0, 500, 502, 3, 74, 37, 0, 501, 500, 1,
        0, 0, 0, 501, 502, 1, 0, 0, 0, 502, 514, 1, 0, 0, 0, 503, 511, 3, 40, 20, 0, 504, 506,
        5, 4, 0, 0, 505, 507, 3, 74, 37, 0, 506, 505, 1, 0, 0, 0, 506, 507, 1, 0, 0, 0, 507, 508,
        1, 0, 0, 0, 508, 510, 3, 40, 20, 0, 509, 504, 1, 0, 0, 0, 510, 513, 1, 0, 0, 0, 511, 509,
        1, 0, 0, 0, 511, 512, 1, 0, 0, 0, 512, 515, 1, 0, 0, 0, 513, 511, 1, 0, 0, 0, 514, 503,
        1, 0, 0, 0, 514, 515, 1, 0, 0, 0, 515, 517, 1, 0, 0, 0, 516, 518, 3, 74, 37, 0, 517, 516,
        1, 0, 0, 0, 517, 518, 1, 0, 0, 0, 518, 519, 1, 0, 0, 0, 519, 520, 5, 5, 0, 0, 520, 77, 1,
        0, 0, 0, 521, 529, 3, 80, 40, 0, 522, 529, 5, 54, 0, 0, 523, 529, 5, 51, 0, 0, 524, 529,
        5, 55, 0, 0, 525, 529, 5, 33, 0, 0, 526, 529, 5, 34, 0, 0, 527, 529, 5, 35, 0, 0, 528,
        521, 1, 0, 0, 0, 528, 522, 1, 0, 0, 0, 528, 523, 1, 0, 0, 0, 528, 524, 1, 0, 0, 0, 528,
        525, 1, 0, 0, 0, 528, 526, 1, 0, 0, 0, 528, 527, 1, 0, 0, 0, 529, 79, 1, 0, 0, 0, 530, 534,
        5, 56, 0, 0, 531, 534, 5, 57, 0, 0, 532, 534, 3, 90, 45, 0, 533, 530, 1, 0, 0, 0, 533,
        531, 1, 0, 0, 0, 533, 532, 1, 0, 0, 0, 534, 536, 1, 0, 0, 0, 535, 537, 5, 53, 0, 0, 536,
        535, 1, 0, 0, 0, 536, 537, 1, 0, 0, 0, 537, 81, 1, 0, 0, 0, 538, 542, 3, 84, 42, 0, 539,
        542, 3, 98, 49, 0, 540, 542, 5, 36, 0, 0, 541, 538, 1, 0, 0, 0, 541, 539, 1, 0, 0, 0, 541,
        540, 1, 0, 0, 0, 542, 83, 1, 0, 0, 0, 543, 551, 5, 37, 0, 0, 544, 551, 5, 38, 0, 0, 545,
        551, 5, 39, 0, 0, 546, 551, 5, 40, 0, 0, 547, 551, 5, 41, 0, 0, 548, 551, 3, 86, 43, 0,
        549, 551, 3, 94, 47, 0, 550, 543, 1, 0, 0, 0, 550, 544, 1, 0, 0, 0, 550, 545, 1, 0, 0,
        0, 550, 546, 1, 0, 0, 0, 550, 547, 1, 0, 0, 0, 550, 548, 1, 0, 0, 0, 550, 549, 1, 0, 0,
        0, 551, 85, 1, 0, 0, 0, 552, 555, 3, 88, 44, 0, 553, 555, 3, 92, 46, 0, 554, 552, 1, 0,
        0, 0, 554, 553, 1, 0, 0, 0, 555, 87, 1, 0, 0, 0, 556, 557, 7, 1, 0, 0, 557, 89, 1, 0, 0,
        0, 558, 559, 5, 56, 0, 0, 559, 560, 7, 2, 0, 0, 560, 561, 5, 56, 0, 0, 561, 567, 5, 18,
        0, 0, 562, 563, 5, 57, 0, 0, 563, 564, 7, 2, 0, 0, 564, 565, 5, 57, 0, 0, 565, 567, 5,
        18, 0, 0, 566, 558, 1, 0, 0, 0, 566, 562, 1, 0, 0, 0, 567, 91, 1, 0, 0, 0, 568, 573, 5,
        45, 0, 0, 569, 570, 5, 9, 0, 0, 570, 571, 3, 88, 44, 0, 571, 572, 5, 10, 0, 0, 572, 574,
        1, 0, 0, 0, 573, 569, 1, 0, 0, 0, 573, 574, 1, 0, 0, 0, 574, 578, 1, 0, 0, 0, 575, 576,
        5, 6, 0, 0, 576, 577, 5, 56, 0, 0, 577, 579, 5, 7, 0, 0, 578, 575, 1, 0, 0, 0, 578, 579,
        1, 0, 0, 0, 579, 596, 1, 0, 0, 0, 580, 585, 5, 46, 0, 0, 581, 582, 5, 9, 0, 0, 582, 583,
        3, 88, 44, 0, 583, 584, 5, 10, 0, 0, 584, 586, 1, 0, 0, 0, 585, 581, 1, 0, 0, 0, 585, 586,
        1, 0, 0, 0, 586, 592, 1, 0, 0, 0, 587, 588, 5, 6, 0, 0, 588, 589, 5, 56, 0, 0, 589, 591,
        5, 7, 0, 0, 590, 587, 1, 0, 0, 0, 591, 594, 1, 0, 0, 0, 592, 590, 1, 0, 0, 0, 592, 593,
        1, 0, 0, 0, 593, 596, 1, 0, 0, 0, 594, 592, 1, 0, 0, 0, 595, 568, 1, 0, 0, 0, 595, 580,
        1, 0, 0, 0, 596, 93, 1, 0, 0, 0, 597, 609, 5, 47, 0, 0, 598, 599, 5, 9, 0, 0, 599, 604,
        3, 96, 48, 0, 600, 601, 5, 4, 0, 0, 601, 603, 3, 96, 48, 0, 602, 600, 1, 0, 0, 0, 603,
        606, 1, 0, 0, 0, 604, 602, 1, 0, 0, 0, 604, 605, 1, 0, 0, 0, 605, 607, 1, 0, 0, 0, 606,
        604, 1, 0, 0, 0, 607, 608, 5, 10, 0, 0, 608, 610, 1, 0, 0, 0, 609, 598, 1, 0, 0, 0, 609,
        610, 1, 0, 0, 0, 610, 614, 1, 0, 0, 0, 611, 612, 5, 6, 0, 0, 612, 613, 5, 56, 0, 0, 613,
        615, 5, 7, 0, 0, 614, 611, 1, 0, 0, 0, 614, 615, 1, 0, 0, 0, 615, 626, 1, 0, 0, 0, 616,
        623, 5, 48, 0, 0, 617, 618, 5, 9, 0, 0, 618, 619, 3, 82, 41, 0, 619, 620, 5, 4, 0, 0, 620,
        621, 3, 96, 48, 0, 621, 622, 5, 10, 0, 0, 622, 624, 1, 0, 0, 0, 623, 617, 1, 0, 0, 0, 623,
        624, 1, 0, 0, 0, 624, 626, 1, 0, 0, 0, 625, 597, 1, 0, 0, 0, 625, 616, 1, 0, 0, 0, 626,
        95, 1, 0, 0, 0, 627, 629, 3, 82, 41, 0, 628, 630, 5, 19, 0, 0, 629, 628, 1, 0, 0, 0, 629,
        630, 1, 0, 0, 0, 630, 97, 1, 0, 0, 0, 631, 632, 5, 52, 0, 0, 632, 99, 1, 0, 0, 0, 99, 101,
        104, 109, 118, 124, 127, 135, 143, 146, 150, 158, 161, 164, 172, 176, 183, 190,
        201, 220, 227, 233, 238, 243, 248, 252, 258, 263, 268, 272, 278, 283, 288, 291,
        294, 300, 304, 309, 314, 317, 320, 326, 332, 342, 346, 351, 356, 361, 364, 367,
        373, 378, 383, 386, 389, 395, 400, 405, 408, 411, 417, 422, 427, 430, 433, 439,
        442, 449, 454, 458, 465, 468, 475, 482, 487, 492, 497, 501, 506, 511, 514, 517,
        528, 533, 536, 541, 550, 554, 566, 573, 578, 585, 592, 595, 604, 609, 614, 623,
        625, 629
    ]


class PslParser(Parser):
    grammarFileName = "Psl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "':'", "'='", "'('", "','", "')'", "'['",
                    "']'", "'@'", "'<'", "'>'", "'{'", "'}'", "'.'", "'->'",
                    "';'", "'+'", "'-'", "'i'", "'?'", "'as'", "'let'",
                    "'use'", "'func'", "'type'", "'enum'", "'with'", "'return'",
                    "'inner'", "'sync'", "'scoped'", "'static'", "'atomic'",
                    "'null'", "'true'", "'false'", "'any'", "'number'",
                    "'string'", "'bool'", "'functor'", "'block'", "'int'",
                    "'real'", "'complex'", "'array'", "'matrix'", "'list'",
                    "'dict'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "AS", "LET", "USE", "FUNC", "TYPE", "ENUM", "WITH",
                     "RETURN", "INNER", "SYNC", "SCOPED", "STATIC", "ATOMIC",
                     "NULL", "TRUE", "FALSE", "ANY_TYPE", "NUMBER_TYPE",
                     "STRING_TYPE", "BOOLEAN_TYPE", "FUNCTOR_TYPE", "BLOCK_TYPE",
                     "INTEGER_TYPE", "REAL_TYPE", "COMPLEX_TYPE", "ARRAY_TYPE",
                     "MATRIX_TYPE", "LIST_TYPE", "DICT_TYPE", "SKIP_",
                     "LINE_END", "MULTI_STR", "IDENTIFIER", "UNIT", "STRING",
                     "FSTRING", "INTEGER", "REAL"]

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
    RULE_type = 41
    RULE_innerType = 42
    RULE_numberType = 43
    RULE_scalarType = 44
    RULE_complex = 45
    RULE_vectorType = 46
    RULE_structType = 47
    RULE_nullableType = 48
    RULE_identRef = 49

    ruleNames = ["program", "stmtList", "stmt", "letStmt", "useStmt",
                 "withDef", "funcDef", "typeDef", "enumDef", "retStmt",
                 "exprStmt", "carrier", "biasAnno", "sizeAnno", "annotation",
                 "annotations", "modifiers", "withList", "withDecl", "paramDef",
                 "argument", "typePack", "keyValDecl", "keyValExpr", "entityRef",
                 "listUnpack", "dictUnpack", "dictPack", "listPack", "stmtPack",
                 "entityExpr", "entityChain", "chainUnit", "entity", "linkCall",
                 "functorRef", "stmtEnd", "sepMark", "argsList", "literal",
                 "value", "type", "innerType", "numberType", "scalarType",
                 "complex", "vectorType", "structType", "nullableType",
                 "identRef"]

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
    AS = 20
    LET = 21
    USE = 22
    FUNC = 23
    TYPE = 24
    ENUM = 25
    WITH = 26
    RETURN = 27
    INNER = 28
    SYNC = 29
    SCOPED = 30
    STATIC = 31
    ATOMIC = 32
    NULL = 33
    TRUE = 34
    FALSE = 35
    ANY_TYPE = 36
    NUMBER_TYPE = 37
    STRING_TYPE = 38
    BOOLEAN_TYPE = 39
    FUNCTOR_TYPE = 40
    BLOCK_TYPE = 41
    INTEGER_TYPE = 42
    REAL_TYPE = 43
    COMPLEX_TYPE = 44
    ARRAY_TYPE = 45
    MATRIX_TYPE = 46
    LIST_TYPE = 47
    DICT_TYPE = 48
    SKIP_ = 49
    LINE_END = 50
    MULTI_STR = 51
    IDENTIFIER = 52
    UNIT = 53
    STRING = 54
    FSTRING = 55
    INTEGER = 56
    REAL = 57

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
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 278097345707510080) != 0):
                self.state = 100
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
            self.state = 107
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 103
                        self.sepMark()

                    self.state = 106
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 109
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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmt"):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)

    def stmt(self):

        localctx = PslParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.letStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.useStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.funcDef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.typeDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.enumDef()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.retStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 117
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
            self.state = 120
            self.match(PslParser.LET)
            self.state = 121
            self.carrier()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 1:
                self.state = 122
                self.match(PslParser.T__0)
                self.state = 123
                self.type_()

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 126
                self.match(PslParser.T__1)

            self.state = 129
            self.entityExpr()
            self.state = 130
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
            self.state = 132
            self.match(PslParser.USE)
            self.state = 133
            self.carrier()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 134
                self.match(PslParser.T__1)

            self.state = 137
            self.entityExpr()
            self.state = 138
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
            self.state = 140
            self.match(PslParser.WITH)
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.state = 141
                self.identRef()
                pass
            elif token in [9]:
                self.state = 142
                self.withDecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 145
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
            self.state = 148
            self.annotations()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 26:
                self.state = 149
                self.withDef()

            self.state = 152
            self.modifiers()
            self.state = 153
            self.match(PslParser.FUNC)
            self.state = 154
            self.identRef()
            self.state = 155
            self.paramDef()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 1:
                self.state = 156
                self.match(PslParser.T__0)
                self.state = 157
                self.type_()

            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 160
                self.match(PslParser.T__1)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 163
                self.match(PslParser.LINE_END)

            self.state = 166
            self.stmtPack()
            self.state = 167
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
            self.state = 169
            self.match(PslParser.TYPE)
            self.state = 170
            self.identRef()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 171
                self.match(PslParser.T__1)

            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 52]:
                self.state = 174
                self.type_()
                pass
            elif token in [11]:
                self.state = 175
                self.typePack()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
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
            self.state = 180
            self.match(PslParser.ENUM)
            self.state = 181
            self.identRef()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 182
                self.match(PslParser.T__1)

            self.state = 185
            self.dictUnpack()
            self.state = 186
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
            self.state = 188
            self.match(PslParser.RETURN)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 276971437212829760) != 0):
                self.state = 189
                self.entityExpr()

            self.state = 192
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
            self.state = 194
            self.annotations()
            self.state = 195
            self.entityExpr()
            self.state = 196
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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCarrier"):
                return visitor.visitCarrier(self)
            else:
                return visitor.visitChildren(self)

    def carrier(self):

        localctx = PslParser.CarrierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_carrier)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.entityRef()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.listUnpack()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
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
            self.state = 203
            self.match(PslParser.T__2)
            self.state = 204
            self.match(PslParser.INTEGER)
            self.state = 205
            self.match(PslParser.T__3)
            self.state = 206
            self.match(PslParser.INTEGER)
            self.state = 207
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
            self.state = 209
            self.match(PslParser.T__5)
            self.state = 210
            self.match(PslParser.INTEGER)
            self.state = 211
            self.match(PslParser.T__3)
            self.state = 212
            self.match(PslParser.INTEGER)
            self.state = 213
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
            self.state = 215
            self.match(PslParser.T__7)
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.state = 216
                self.identRef()
                pass
            elif token in [11]:
                self.state = 217
                self.dictPack()
                pass
            elif token in [3]:
                self.state = 218
                self.biasAnno()
                pass
            elif token in [6]:
                self.state = 219
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
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 8:
                self.state = 222
                self.annotation()
                self.state = 223
                self.match(PslParser.LINE_END)
                self.state = 229
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

        def INNER(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.INNER)
            else:
                return self.getToken(PslParser.INNER, i)

        def SYNC(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.SYNC)
            else:
                return self.getToken(PslParser.SYNC, i)

        def SCOPED(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.SCOPED)
            else:
                return self.getToken(PslParser.SCOPED, i)

        def STATIC(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.STATIC)
            else:
                return self.getToken(PslParser.STATIC, i)

        def ATOMIC(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.ATOMIC)
            else:
                return self.getToken(PslParser.ATOMIC, i)

        def getRuleIndex(self):
            return PslParser.RULE_modifiers

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
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0):
                self.state = 230
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 235
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
            self.state = 236
            self.match(PslParser.T__8)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 237
                self.sepMark()

            self.state = 240
            self.argument()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 241
                self.match(PslParser.T__3)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 50:
                    self.state = 242
                    self.sepMark()

                self.state = 245
                self.argument()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 251
                self.sepMark()

            self.state = 254
            self.match(PslParser.T__9)
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
            self.state = 256
            self.match(PslParser.T__8)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 257
                self.sepMark()

            self.state = 260
            self.keyValDecl()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 261
                self.match(PslParser.T__3)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 50:
                    self.state = 262
                    self.sepMark()

                self.state = 265
                self.keyValDecl()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 271
                self.sepMark()

            self.state = 274
            self.match(PslParser.T__9)
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
            self.state = 276
            self.match(PslParser.T__2)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 29, self._ctx)
            if la_ == 1:
                self.state = 277
                self.sepMark()

            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 280
                self.keyValDecl()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 281
                    self.match(PslParser.T__3)
                    self.state = 283
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 282
                        self.sepMark()

                    self.state = 285
                    self.keyValDecl()
                    self.state = 290
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 293
                self.sepMark()

            self.state = 296
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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArgument"):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)

    def argument(self):

        localctx = PslParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_argument)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 34, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.entityExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
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
            self.state = 302
            self.match(PslParser.T__10)
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 35, self._ctx)
            if la_ == 1:
                self.state = 303
                self.sepMark()

            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 306
                self.keyValDecl()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 307
                    self.match(PslParser.T__3)
                    self.state = 309
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 308
                        self.sepMark()

                    self.state = 311
                    self.keyValDecl()
                    self.state = 316
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 319
                self.sepMark()

            self.state = 322
            self.match(PslParser.T__11)
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
            self.state = 324
            self.identRef()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 8:
                self.state = 325
                self.annotation()

            self.state = 328
            self.match(PslParser.T__0)
            self.state = 329
            self.nullableType()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 330
                self.match(PslParser.T__1)
                self.state = 331
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
            self.state = 334
            self.identRef()
            self.state = 335
            self.match(PslParser.T__1)
            self.state = 336
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
            self.state = 338
            self.identRef()
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 43, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 339
                    self.match(PslParser.T__12)
                    self.state = 342
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [56]:
                        self.state = 340
                        self.match(PslParser.INTEGER)
                        pass
                    elif token in [52]:
                        self.state = 341
                        self.identRef()
                        pass
                    else:
                        raise NoViableAltException(self)

                self.state = 348
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
            self.state = 349
            self.match(PslParser.T__5)
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 44, self._ctx)
            if la_ == 1:
                self.state = 350
                self.sepMark()

            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 353
                self.identRef()
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 354
                    self.match(PslParser.T__3)
                    self.state = 356
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 355
                        self.sepMark()

                    self.state = 358
                    self.identRef()
                    self.state = 363
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 366
                self.sepMark()

            self.state = 369
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
            self.state = 371
            self.match(PslParser.T__10)
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 49, self._ctx)
            if la_ == 1:
                self.state = 372
                self.sepMark()

            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 375
                self.identRef()
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 376
                    self.match(PslParser.T__3)
                    self.state = 378
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 377
                        self.sepMark()

                    self.state = 380
                    self.identRef()
                    self.state = 385
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 388
                self.sepMark()

            self.state = 391
            self.match(PslParser.T__11)
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
            self.state = 393
            self.match(PslParser.T__10)
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 54, self._ctx)
            if la_ == 1:
                self.state = 394
                self.sepMark()

            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 52:
                self.state = 397
                self.keyValExpr()
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 398
                    self.match(PslParser.T__3)
                    self.state = 400
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 399
                        self.sepMark()

                    self.state = 402
                    self.keyValExpr()
                    self.state = 407
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 410
                self.sepMark()

            self.state = 413
            self.match(PslParser.T__11)
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
            self.state = 415
            self.match(PslParser.T__5)
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 59, self._ctx)
            if la_ == 1:
                self.state = 416
                self.sepMark()

            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 276971437212829760) != 0):
                self.state = 419
                self.entityExpr()
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 420
                    self.match(PslParser.T__3)
                    self.state = 422
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 421
                        self.sepMark()

                    self.state = 424
                    self.entityExpr()
                    self.state = 429
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 432
                self.sepMark()

            self.state = 435
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
            self.state = 437
            self.match(PslParser.T__10)
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 64, self._ctx)
            if la_ == 1:
                self.state = 438
                self.stmtList()

            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 441
                self.sepMark()

            self.state = 444
            self.match(PslParser.T__11)
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

        def AS(self):
            return self.getToken(PslParser.AS, 0)

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_entityExpr

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
            self.state = 446
            self.entityChain()
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 20:
                self.state = 447
                self.match(PslParser.AS)
                self.state = 448
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
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 451
                self.chainUnit()
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 276971437212829760) != 0)):
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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitChainUnit"):
                return visitor.visitChainUnit(self)
            else:
                return visitor.visitChildren(self)

    def chainUnit(self):

        localctx = PslParser.ChainUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_chainUnit)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 68, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
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
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 69, self._ctx)
            if la_ == 1:
                self.state = 460
                self.entityRef()
                pass

            elif la_ == 2:
                self.state = 461
                self.functorRef()
                pass

            elif la_ == 3:
                self.state = 462
                self.literal()
                pass

            elif la_ == 4:
                self.state = 463
                self.listPack()
                pass

            elif la_ == 5:
                self.state = 464
                self.dictPack()
                pass

            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 70, self._ctx)
            if la_ == 1:
                self.state = 467
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
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 71, self._ctx)
            if la_ == 1:
                self.state = 471
                self.functorRef()
                self.state = 472
                self.argsList()
                pass

            elif la_ == 2:
                self.state = 474
                self.entity()
                pass

            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 72, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PslParser.LinkCallContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_linkCall)
                    self.state = 477
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 478
                    self.match(PslParser.T__13)
                    self.state = 479
                    self.entity()
                self.state = 484
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
            self.state = 485
            self.identRef()
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 73, self._ctx)
            if la_ == 1:
                self.state = 486
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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmtEnd"):
                return visitor.visitStmtEnd(self)
            else:
                return visitor.visitChildren(self)

    def stmtEnd(self):

        localctx = PslParser.StmtEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmtEnd)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.sepMark()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.match(PslParser.T__14)
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
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
            self.state = 495
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 494
                    self.match(PslParser.LINE_END)

                else:
                    raise NoViableAltException(self)
                self.state = 497
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
            self.state = 499
            self.match(PslParser.T__2)
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 76, self._ctx)
            if la_ == 1:
                self.state = 500
                self.sepMark()

            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 276971437212829760) != 0):
                self.state = 503
                self.argument()
                self.state = 511
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 504
                    self.match(PslParser.T__3)
                    self.state = 506
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 50:
                        self.state = 505
                        self.sepMark()

                    self.state = 508
                    self.argument()
                    self.state = 513
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 50:
                self.state = 516
                self.sepMark()

            self.state = 519
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

        def FSTRING(self):
            return self.getToken(PslParser.FSTRING, 0)

        def NULL(self):
            return self.getToken(PslParser.NULL, 0)

        def TRUE(self):
            return self.getToken(PslParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PslParser.FALSE, 0)

        def getRuleIndex(self):
            return PslParser.RULE_literal

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLiteral"):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)

    def literal(self):

        localctx = PslParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.value()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(PslParser.STRING)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(PslParser.MULTI_STR)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.match(PslParser.FSTRING)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 525
                self.match(PslParser.NULL)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 526
                self.match(PslParser.TRUE)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 7)
                self.state = 527
                self.match(PslParser.FALSE)
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
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 82, self._ctx)
            if la_ == 1:
                self.state = 530
                self.match(PslParser.INTEGER)
                pass

            elif la_ == 2:
                self.state = 531
                self.match(PslParser.REAL)
                pass

            elif la_ == 3:
                self.state = 532
                self.complex_()
                pass

            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 83, self._ctx)
            if la_ == 1:
                self.state = 535
                self.match(PslParser.UNIT)


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

        def ANY_TYPE(self):
            return self.getToken(PslParser.ANY_TYPE, 0)

        def getRuleIndex(self):
            return PslParser.RULE_type

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitType"):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)

    def type_(self):

        localctx = PslParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_type)
        try:
            self.state = 541
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.innerType()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.identRef()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.match(PslParser.ANY_TYPE)
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

        def NUMBER_TYPE(self):
            return self.getToken(PslParser.NUMBER_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(PslParser.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(PslParser.BOOLEAN_TYPE, 0)

        def FUNCTOR_TYPE(self):
            return self.getToken(PslParser.FUNCTOR_TYPE, 0)

        def BLOCK_TYPE(self):
            return self.getToken(PslParser.BLOCK_TYPE, 0)

        def numberType(self):
            return self.getTypedRuleContext(PslParser.NumberTypeContext, 0)

        def structType(self):
            return self.getTypedRuleContext(PslParser.StructTypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_innerType

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitInnerType"):
                return visitor.visitInnerType(self)
            else:
                return visitor.visitChildren(self)

    def innerType(self):

        localctx = PslParser.InnerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_innerType)
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.match(PslParser.NUMBER_TYPE)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.match(PslParser.STRING_TYPE)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 545
                self.match(PslParser.BOOLEAN_TYPE)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 546
                self.match(PslParser.FUNCTOR_TYPE)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 5)
                self.state = 547
                self.match(PslParser.BLOCK_TYPE)
                pass
            elif token in [42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 6)
                self.state = 548
                self.numberType()
                pass
            elif token in [47, 48]:
                self.enterOuterAlt(localctx, 7)
                self.state = 549
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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNumberType"):
                return visitor.visitNumberType(self)
            else:
                return visitor.visitChildren(self)

    def numberType(self):

        localctx = PslParser.NumberTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_numberType)
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.scalarType()
                pass
            elif token in [45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
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

        def INTEGER_TYPE(self):
            return self.getToken(PslParser.INTEGER_TYPE, 0)

        def REAL_TYPE(self):
            return self.getToken(PslParser.REAL_TYPE, 0)

        def COMPLEX_TYPE(self):
            return self.getToken(PslParser.COMPLEX_TYPE, 0)

        def getRuleIndex(self):
            return PslParser.RULE_scalarType

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitScalarType"):
                return visitor.visitScalarType(self)
            else:
                return visitor.visitChildren(self)

    def scalarType(self):

        localctx = PslParser.ScalarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_scalarType)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577728) != 0)):
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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitComplex"):
                return visitor.visitComplex(self)
            else:
                return visitor.visitChildren(self)

    def complex_(self):

        localctx = PslParser.ComplexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_complex)
        self._la = 0  # Token type
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.match(PslParser.INTEGER)
                self.state = 559
                _la = self._input.LA(1)
                if not (_la == 16 or _la == 17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 560
                self.match(PslParser.INTEGER)
                self.state = 561
                self.match(PslParser.T__17)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.match(PslParser.REAL)
                self.state = 563
                _la = self._input.LA(1)
                if not (_la == 16 or _la == 17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 564
                self.match(PslParser.REAL)
                self.state = 565
                self.match(PslParser.T__17)
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

    class VectorTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_TYPE(self):
            return self.getToken(PslParser.ARRAY_TYPE, 0)

        def scalarType(self):
            return self.getTypedRuleContext(PslParser.ScalarTypeContext, 0)

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(PslParser.INTEGER)
            else:
                return self.getToken(PslParser.INTEGER, i)

        def MATRIX_TYPE(self):
            return self.getToken(PslParser.MATRIX_TYPE, 0)

        def getRuleIndex(self):
            return PslParser.RULE_vectorType

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVectorType"):
                return visitor.visitVectorType(self)
            else:
                return visitor.visitChildren(self)

    def vectorType(self):

        localctx = PslParser.VectorTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_vectorType)
        self._la = 0  # Token type
        try:
            self.state = 595
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.match(PslParser.ARRAY_TYPE)
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 569
                    self.match(PslParser.T__8)
                    self.state = 570
                    self.scalarType()
                    self.state = 571
                    self.match(PslParser.T__9)

                self.state = 578
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 89, self._ctx)
                if la_ == 1:
                    self.state = 575
                    self.match(PslParser.T__5)
                    self.state = 576
                    self.match(PslParser.INTEGER)
                    self.state = 577
                    self.match(PslParser.T__6)

                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
                self.match(PslParser.MATRIX_TYPE)
                self.state = 585
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 581
                    self.match(PslParser.T__8)
                    self.state = 582
                    self.scalarType()
                    self.state = 583
                    self.match(PslParser.T__9)

                self.state = 592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 91, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 587
                        self.match(PslParser.T__5)
                        self.state = 588
                        self.match(PslParser.INTEGER)
                        self.state = 589
                        self.match(PslParser.T__6)
                    self.state = 594
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

        def LIST_TYPE(self):
            return self.getToken(PslParser.LIST_TYPE, 0)

        def nullableType(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PslParser.NullableTypeContext)
            else:
                return self.getTypedRuleContext(PslParser.NullableTypeContext, i)

        def INTEGER(self):
            return self.getToken(PslParser.INTEGER, 0)

        def DICT_TYPE(self):
            return self.getToken(PslParser.DICT_TYPE, 0)

        def type_(self):
            return self.getTypedRuleContext(PslParser.TypeContext, 0)

        def getRuleIndex(self):
            return PslParser.RULE_structType

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStructType"):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)

    def structType(self):

        localctx = PslParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_structType)
        self._la = 0  # Token type
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 597
                self.match(PslParser.LIST_TYPE)
                self.state = 609
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 598
                    self.match(PslParser.T__8)
                    self.state = 599
                    self.nullableType()
                    self.state = 604
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == 4:
                        self.state = 600
                        self.match(PslParser.T__3)
                        self.state = 601
                        self.nullableType()
                        self.state = 606
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 607
                    self.match(PslParser.T__9)

                self.state = 614
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 95, self._ctx)
                if la_ == 1:
                    self.state = 611
                    self.match(PslParser.T__5)
                    self.state = 612
                    self.match(PslParser.INTEGER)
                    self.state = 613
                    self.match(PslParser.T__6)

                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self.match(PslParser.DICT_TYPE)
                self.state = 623
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 617
                    self.match(PslParser.T__8)
                    self.state = 618
                    self.type_()
                    self.state = 619
                    self.match(PslParser.T__3)
                    self.state = 620
                    self.nullableType()
                    self.state = 621
                    self.match(PslParser.T__9)

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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNullableType"):
                return visitor.visitNullableType(self)
            else:
                return visitor.visitChildren(self)

    def nullableType(self):

        localctx = PslParser.NullableTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_nullableType)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.type_()
            self.state = 629
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 19:
                self.state = 628
                self.match(PslParser.T__18)


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

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdentRef"):
                return visitor.visitIdentRef(self)
            else:
                return visitor.visitChildren(self)

    def identRef(self):

        localctx = PslParser.IdentRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_identRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
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
