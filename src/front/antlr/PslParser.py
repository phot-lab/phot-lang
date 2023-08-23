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
        4, 1, 56, 626, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 2, 20,
        7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2, 26, 7, 26,
        2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 2, 30, 7, 30, 2, 31, 7, 31, 2, 32, 7, 32, 2, 33,
        7, 33, 2, 34, 7, 34, 2, 35, 7, 35, 2, 36, 7, 36, 2, 37, 7, 37, 2, 38, 7, 38, 2, 39, 7, 39,
        2, 40, 7, 40, 2, 41, 7, 41, 2, 42, 7, 42, 2, 43, 7, 43, 2, 44, 7, 44, 2, 45, 7, 45, 2, 46,
        7, 46, 2, 47, 7, 47, 2, 48, 7, 48, 1, 0, 3, 0, 100, 8, 0, 1, 1, 3, 1, 103, 8, 1, 1, 1, 4, 1,
        106, 8, 1, 11, 1, 12, 1, 107, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 117, 8, 2, 1,
        3, 1, 3, 1, 3, 1, 3, 3, 3, 123, 8, 3, 1, 3, 3, 3, 126, 8, 3, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1,
        4, 3, 4, 134, 8, 4, 1, 4, 1, 4, 1, 4, 1, 5, 1, 5, 1, 5, 3, 5, 142, 8, 5, 1, 5, 3, 5, 145, 8,
        5, 1, 6, 1, 6, 3, 6, 149, 8, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 3, 6, 157, 8, 6, 1, 6, 3,
        6, 160, 8, 6, 1, 6, 3, 6, 163, 8, 6, 1, 6, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 3, 7, 171, 8, 7, 1,
        7, 1, 7, 3, 7, 175, 8, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 3, 8, 182, 8, 8, 1, 8, 1, 8, 1, 8, 1,
        9, 1, 9, 3, 9, 189, 8, 9, 1, 9, 1, 9, 1, 10, 1, 10, 1, 10, 1, 10, 1, 11, 1, 11, 1, 11, 3, 11,
        200, 8, 11, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13,
        1, 13, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14, 3, 14, 219, 8, 14, 1, 15, 1, 15, 1, 15, 5, 15,
        224, 8, 15, 10, 15, 12, 15, 227, 9, 15, 1, 16, 5, 16, 230, 8, 16, 10, 16, 12, 16, 233,
        9, 16, 1, 17, 1, 17, 3, 17, 237, 8, 17, 1, 17, 1, 17, 1, 17, 3, 17, 242, 8, 17, 1, 17, 5,
        17, 245, 8, 17, 10, 17, 12, 17, 248, 9, 17, 1, 17, 3, 17, 251, 8, 17, 1, 17, 1, 17, 1,
        18, 1, 18, 3, 18, 257, 8, 18, 1, 18, 1, 18, 1, 18, 3, 18, 262, 8, 18, 1, 18, 5, 18, 265,
        8, 18, 10, 18, 12, 18, 268, 9, 18, 1, 18, 3, 18, 271, 8, 18, 1, 18, 1, 18, 1, 19, 1, 19,
        3, 19, 277, 8, 19, 1, 19, 1, 19, 1, 19, 3, 19, 282, 8, 19, 1, 19, 5, 19, 285, 8, 19, 10,
        19, 12, 19, 288, 9, 19, 3, 19, 290, 8, 19, 1, 19, 3, 19, 293, 8, 19, 1, 19, 1, 19, 1, 20,
        1, 20, 3, 20, 299, 8, 20, 1, 21, 1, 21, 3, 21, 303, 8, 21, 1, 21, 1, 21, 1, 21, 3, 21, 308,
        8, 21, 1, 21, 5, 21, 311, 8, 21, 10, 21, 12, 21, 314, 9, 21, 3, 21, 316, 8, 21, 1, 21,
        3, 21, 319, 8, 21, 1, 21, 1, 21, 1, 22, 1, 22, 3, 22, 325, 8, 22, 1, 22, 1, 22, 1, 22, 1,
        22, 3, 22, 331, 8, 22, 1, 23, 1, 23, 1, 23, 1, 23, 1, 24, 1, 24, 1, 24, 1, 24, 3, 24, 341,
        8, 24, 1, 24, 5, 24, 344, 8, 24, 10, 24, 12, 24, 347, 9, 24, 1, 24, 1, 24, 1, 24, 3, 24,
        352, 8, 24, 3, 24, 354, 8, 24, 1, 25, 1, 25, 3, 25, 358, 8, 25, 1, 25, 1, 25, 1, 25, 3,
        25, 363, 8, 25, 1, 25, 5, 25, 366, 8, 25, 10, 25, 12, 25, 369, 9, 25, 3, 25, 371, 8, 25,
        1, 25, 3, 25, 374, 8, 25, 1, 25, 1, 25, 1, 26, 1, 26, 3, 26, 380, 8, 26, 1, 26, 1, 26, 1,
        26, 3, 26, 385, 8, 26, 1, 26, 5, 26, 388, 8, 26, 10, 26, 12, 26, 391, 9, 26, 3, 26, 393,
        8, 26, 1, 26, 3, 26, 396, 8, 26, 1, 26, 1, 26, 1, 27, 1, 27, 3, 27, 402, 8, 27, 1, 27, 1,
        27, 1, 27, 3, 27, 407, 8, 27, 1, 27, 5, 27, 410, 8, 27, 10, 27, 12, 27, 413, 9, 27, 3,
        27, 415, 8, 27, 1, 27, 3, 27, 418, 8, 27, 1, 27, 1, 27, 1, 28, 1, 28, 3, 28, 424, 8, 28,
        1, 28, 1, 28, 1, 28, 3, 28, 429, 8, 28, 1, 28, 5, 28, 432, 8, 28, 10, 28, 12, 28, 435,
        9, 28, 3, 28, 437, 8, 28, 1, 28, 3, 28, 440, 8, 28, 1, 28, 1, 28, 1, 29, 1, 29, 3, 29, 446,
        8, 29, 1, 29, 3, 29, 449, 8, 29, 1, 29, 1, 29, 1, 30, 1, 30, 1, 30, 3, 30, 456, 8, 30, 1,
        31, 4, 31, 459, 8, 31, 11, 31, 12, 31, 460, 1, 32, 1, 32, 3, 32, 465, 8, 32, 1, 33, 1,
        33, 1, 33, 1, 33, 1, 33, 3, 33, 472, 8, 33, 1, 33, 3, 33, 475, 8, 33, 1, 34, 1, 34, 1, 34,
        1, 34, 1, 34, 3, 34, 482, 8, 34, 1, 34, 1, 34, 1, 34, 5, 34, 487, 8, 34, 10, 34, 12, 34,
        490, 9, 34, 1, 35, 1, 35, 3, 35, 494, 8, 35, 1, 36, 1, 36, 1, 36, 3, 36, 499, 8, 36, 1,
        37, 4, 37, 502, 8, 37, 11, 37, 12, 37, 503, 1, 38, 1, 38, 3, 38, 508, 8, 38, 1, 38, 1,
        38, 1, 38, 3, 38, 513, 8, 38, 1, 38, 5, 38, 516, 8, 38, 10, 38, 12, 38, 519, 9, 38, 3,
        38, 521, 8, 38, 1, 38, 3, 38, 524, 8, 38, 1, 38, 1, 38, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39,
        1, 39, 1, 39, 3, 39, 535, 8, 39, 1, 40, 1, 40, 3, 40, 539, 8, 40, 1, 41, 1, 41, 1, 41, 3,
        41, 544, 8, 41, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 3, 42, 553, 8, 42, 1, 43,
        1, 43, 3, 43, 557, 8, 43, 1, 44, 1, 44, 1, 45, 1, 45, 1, 45, 1, 45, 1, 45, 3, 45, 566, 8,
        45, 1, 45, 1, 45, 1, 45, 3, 45, 571, 8, 45, 1, 45, 1, 45, 1, 45, 1, 45, 1, 45, 3, 45, 578,
        8, 45, 1, 45, 1, 45, 1, 45, 5, 45, 583, 8, 45, 10, 45, 12, 45, 586, 9, 45, 3, 45, 588,
        8, 45, 1, 46, 1, 46, 1, 46, 1, 46, 1, 46, 5, 46, 595, 8, 46, 10, 46, 12, 46, 598, 9, 46,
        1, 46, 1, 46, 3, 46, 602, 8, 46, 1, 46, 1, 46, 1, 46, 3, 46, 607, 8, 46, 1, 46, 1, 46, 1,
        46, 1, 46, 1, 46, 1, 46, 1, 46, 3, 46, 616, 8, 46, 3, 46, 618, 8, 46, 1, 47, 1, 47, 3, 47,
        622, 8, 47, 1, 48, 1, 48, 1, 48, 0, 1, 68, 49, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22,
        24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66,
        68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 0, 3, 1, 0, 25, 29, 1, 0, 53,
        55, 1, 0, 39, 41, 698, 0, 99, 1, 0, 0, 0, 2, 105, 1, 0, 0, 0, 4, 116, 1, 0, 0, 0, 6, 118,
        1, 0, 0, 0, 8, 130, 1, 0, 0, 0, 10, 138, 1, 0, 0, 0, 12, 146, 1, 0, 0, 0, 14, 167, 1, 0, 0,
        0, 16, 178, 1, 0, 0, 0, 18, 186, 1, 0, 0, 0, 20, 192, 1, 0, 0, 0, 22, 199, 1, 0, 0, 0, 24,
        201, 1, 0, 0, 0, 26, 207, 1, 0, 0, 0, 28, 213, 1, 0, 0, 0, 30, 225, 1, 0, 0, 0, 32, 231,
        1, 0, 0, 0, 34, 234, 1, 0, 0, 0, 36, 254, 1, 0, 0, 0, 38, 274, 1, 0, 0, 0, 40, 298, 1, 0,
        0, 0, 42, 300, 1, 0, 0, 0, 44, 322, 1, 0, 0, 0, 46, 332, 1, 0, 0, 0, 48, 336, 1, 0, 0, 0,
        50, 355, 1, 0, 0, 0, 52, 377, 1, 0, 0, 0, 54, 399, 1, 0, 0, 0, 56, 421, 1, 0, 0, 0, 58, 443,
        1, 0, 0, 0, 60, 452, 1, 0, 0, 0, 62, 458, 1, 0, 0, 0, 64, 464, 1, 0, 0, 0, 66, 471, 1, 0,
        0, 0, 68, 481, 1, 0, 0, 0, 70, 491, 1, 0, 0, 0, 72, 498, 1, 0, 0, 0, 74, 501, 1, 0, 0, 0,
        76, 505, 1, 0, 0, 0, 78, 534, 1, 0, 0, 0, 80, 536, 1, 0, 0, 0, 82, 543, 1, 0, 0, 0, 84, 552,
        1, 0, 0, 0, 86, 556, 1, 0, 0, 0, 88, 558, 1, 0, 0, 0, 90, 587, 1, 0, 0, 0, 92, 617, 1, 0,
        0, 0, 94, 619, 1, 0, 0, 0, 96, 623, 1, 0, 0, 0, 98, 100, 3, 2, 1, 0, 99, 98, 1, 0, 0, 0, 99,
        100, 1, 0, 0, 0, 100, 1, 1, 0, 0, 0, 101, 103, 3, 74, 37, 0, 102, 101, 1, 0, 0, 0, 102,
        103, 1, 0, 0, 0, 103, 104, 1, 0, 0, 0, 104, 106, 3, 4, 2, 0, 105, 102, 1, 0, 0, 0, 106,
        107, 1, 0, 0, 0, 107, 105, 1, 0, 0, 0, 107, 108, 1, 0, 0, 0, 108, 3, 1, 0, 0, 0, 109, 117,
        3, 6, 3, 0, 110, 117, 3, 8, 4, 0, 111, 117, 3, 12, 6, 0, 112, 117, 3, 14, 7, 0, 113, 117,
        3, 16, 8, 0, 114, 117, 3, 18, 9, 0, 115, 117, 3, 20, 10, 0, 116, 109, 1, 0, 0, 0, 116,
        110, 1, 0, 0, 0, 116, 111, 1, 0, 0, 0, 116, 112, 1, 0, 0, 0, 116, 113, 1, 0, 0, 0, 116,
        114, 1, 0, 0, 0, 116, 115, 1, 0, 0, 0, 117, 5, 1, 0, 0, 0, 118, 119, 5, 18, 0, 0, 119, 122,
        3, 22, 11, 0, 120, 121, 5, 1, 0, 0, 121, 123, 3, 82, 41, 0, 122, 120, 1, 0, 0, 0, 122,
        123, 1, 0, 0, 0, 123, 125, 1, 0, 0, 0, 124, 126, 5, 2, 0, 0, 125, 124, 1, 0, 0, 0, 125,
        126, 1, 0, 0, 0, 126, 127, 1, 0, 0, 0, 127, 128, 3, 60, 30, 0, 128, 129, 3, 72, 36, 0,
        129, 7, 1, 0, 0, 0, 130, 131, 5, 19, 0, 0, 131, 133, 3, 22, 11, 0, 132, 134, 5, 2, 0, 0,
        133, 132, 1, 0, 0, 0, 133, 134, 1, 0, 0, 0, 134, 135, 1, 0, 0, 0, 135, 136, 3, 60, 30,
        0, 136, 137, 3, 72, 36, 0, 137, 9, 1, 0, 0, 0, 138, 141, 5, 23, 0, 0, 139, 142, 3, 96,
        48, 0, 140, 142, 3, 36, 18, 0, 141, 139, 1, 0, 0, 0, 141, 140, 1, 0, 0, 0, 142, 144, 1,
        0, 0, 0, 143, 145, 5, 47, 0, 0, 144, 143, 1, 0, 0, 0, 144, 145, 1, 0, 0, 0, 145, 11, 1,
        0, 0, 0, 146, 148, 3, 30, 15, 0, 147, 149, 3, 10, 5, 0, 148, 147, 1, 0, 0, 0, 148, 149,
        1, 0, 0, 0, 149, 150, 1, 0, 0, 0, 150, 151, 3, 32, 16, 0, 151, 152, 5, 20, 0, 0, 152, 153,
        3, 96, 48, 0, 153, 156, 3, 38, 19, 0, 154, 155, 5, 1, 0, 0, 155, 157, 3, 82, 41, 0, 156,
        154, 1, 0, 0, 0, 156, 157, 1, 0, 0, 0, 157, 159, 1, 0, 0, 0, 158, 160, 5, 2, 0, 0, 159,
        158, 1, 0, 0, 0, 159, 160, 1, 0, 0, 0, 160, 162, 1, 0, 0, 0, 161, 163, 5, 47, 0, 0, 162,
        161, 1, 0, 0, 0, 162, 163, 1, 0, 0, 0, 163, 164, 1, 0, 0, 0, 164, 165, 3, 58, 29, 0, 165,
        166, 3, 72, 36, 0, 166, 13, 1, 0, 0, 0, 167, 168, 5, 21, 0, 0, 168, 170, 3, 96, 48, 0,
        169, 171, 5, 2, 0, 0, 170, 169, 1, 0, 0, 0, 170, 171, 1, 0, 0, 0, 171, 174, 1, 0, 0, 0,
        172, 175, 3, 82, 41, 0, 173, 175, 3, 42, 21, 0, 174, 172, 1, 0, 0, 0, 174, 173, 1, 0,
        0, 0, 175, 176, 1, 0, 0, 0, 176, 177, 3, 72, 36, 0, 177, 15, 1, 0, 0, 0, 178, 179, 5, 22,
        0, 0, 179, 181, 3, 96, 48, 0, 180, 182, 5, 2, 0, 0, 181, 180, 1, 0, 0, 0, 181, 182, 1,
        0, 0, 0, 182, 183, 1, 0, 0, 0, 183, 184, 3, 52, 26, 0, 184, 185, 3, 72, 36, 0, 185, 17,
        1, 0, 0, 0, 186, 188, 5, 24, 0, 0, 187, 189, 3, 60, 30, 0, 188, 187, 1, 0, 0, 0, 188, 189,
        1, 0, 0, 0, 189, 190, 1, 0, 0, 0, 190, 191, 3, 72, 36, 0, 191, 19, 1, 0, 0, 0, 192, 193,
        3, 30, 15, 0, 193, 194, 3, 60, 30, 0, 194, 195, 3, 72, 36, 0, 195, 21, 1, 0, 0, 0, 196,
        200, 3, 48, 24, 0, 197, 200, 3, 50, 25, 0, 198, 200, 3, 52, 26, 0, 199, 196, 1, 0, 0,
        0, 199, 197, 1, 0, 0, 0, 199, 198, 1, 0, 0, 0, 200, 23, 1, 0, 0, 0, 201, 202, 5, 3, 0, 0,
        202, 203, 5, 54, 0, 0, 203, 204, 5, 4, 0, 0, 204, 205, 5, 54, 0, 0, 205, 206, 5, 5, 0,
        0, 206, 25, 1, 0, 0, 0, 207, 208, 5, 6, 0, 0, 208, 209, 5, 54, 0, 0, 209, 210, 5, 4, 0,
        0, 210, 211, 5, 54, 0, 0, 211, 212, 5, 7, 0, 0, 212, 27, 1, 0, 0, 0, 213, 218, 5, 8, 0,
        0, 214, 219, 3, 96, 48, 0, 215, 219, 3, 54, 27, 0, 216, 219, 3, 24, 12, 0, 217, 219,
        3, 26, 13, 0, 218, 214, 1, 0, 0, 0, 218, 215, 1, 0, 0, 0, 218, 216, 1, 0, 0, 0, 218, 217,
        1, 0, 0, 0, 219, 29, 1, 0, 0, 0, 220, 221, 3, 28, 14, 0, 221, 222, 5, 47, 0, 0, 222, 224,
        1, 0, 0, 0, 223, 220, 1, 0, 0, 0, 224, 227, 1, 0, 0, 0, 225, 223, 1, 0, 0, 0, 225, 226,
        1, 0, 0, 0, 226, 31, 1, 0, 0, 0, 227, 225, 1, 0, 0, 0, 228, 230, 7, 0, 0, 0, 229, 228, 1,
        0, 0, 0, 230, 233, 1, 0, 0, 0, 231, 229, 1, 0, 0, 0, 231, 232, 1, 0, 0, 0, 232, 33, 1, 0,
        0, 0, 233, 231, 1, 0, 0, 0, 234, 236, 5, 9, 0, 0, 235, 237, 3, 74, 37, 0, 236, 235, 1,
        0, 0, 0, 236, 237, 1, 0, 0, 0, 237, 238, 1, 0, 0, 0, 238, 246, 3, 40, 20, 0, 239, 241,
        5, 4, 0, 0, 240, 242, 3, 74, 37, 0, 241, 240, 1, 0, 0, 0, 241, 242, 1, 0, 0, 0, 242, 243,
        1, 0, 0, 0, 243, 245, 3, 40, 20, 0, 244, 239, 1, 0, 0, 0, 245, 248, 1, 0, 0, 0, 246, 244,
        1, 0, 0, 0, 246, 247, 1, 0, 0, 0, 247, 250, 1, 0, 0, 0, 248, 246, 1, 0, 0, 0, 249, 251,
        3, 74, 37, 0, 250, 249, 1, 0, 0, 0, 250, 251, 1, 0, 0, 0, 251, 252, 1, 0, 0, 0, 252, 253,
        5, 10, 0, 0, 253, 35, 1, 0, 0, 0, 254, 256, 5, 9, 0, 0, 255, 257, 3, 74, 37, 0, 256, 255,
        1, 0, 0, 0, 256, 257, 1, 0, 0, 0, 257, 258, 1, 0, 0, 0, 258, 266, 3, 44, 22, 0, 259, 261,
        5, 4, 0, 0, 260, 262, 3, 74, 37, 0, 261, 260, 1, 0, 0, 0, 261, 262, 1, 0, 0, 0, 262, 263,
        1, 0, 0, 0, 263, 265, 3, 44, 22, 0, 264, 259, 1, 0, 0, 0, 265, 268, 1, 0, 0, 0, 266, 264,
        1, 0, 0, 0, 266, 267, 1, 0, 0, 0, 267, 270, 1, 0, 0, 0, 268, 266, 1, 0, 0, 0, 269, 271,
        3, 74, 37, 0, 270, 269, 1, 0, 0, 0, 270, 271, 1, 0, 0, 0, 271, 272, 1, 0, 0, 0, 272, 273,
        5, 10, 0, 0, 273, 37, 1, 0, 0, 0, 274, 276, 5, 3, 0, 0, 275, 277, 3, 74, 37, 0, 276, 275,
        1, 0, 0, 0, 276, 277, 1, 0, 0, 0, 277, 289, 1, 0, 0, 0, 278, 286, 3, 44, 22, 0, 279, 281,
        5, 4, 0, 0, 280, 282, 3, 74, 37, 0, 281, 280, 1, 0, 0, 0, 281, 282, 1, 0, 0, 0, 282, 283,
        1, 0, 0, 0, 283, 285, 3, 44, 22, 0, 284, 279, 1, 0, 0, 0, 285, 288, 1, 0, 0, 0, 286, 284,
        1, 0, 0, 0, 286, 287, 1, 0, 0, 0, 287, 290, 1, 0, 0, 0, 288, 286, 1, 0, 0, 0, 289, 278,
        1, 0, 0, 0, 289, 290, 1, 0, 0, 0, 290, 292, 1, 0, 0, 0, 291, 293, 3, 74, 37, 0, 292, 291,
        1, 0, 0, 0, 292, 293, 1, 0, 0, 0, 293, 294, 1, 0, 0, 0, 294, 295, 5, 5, 0, 0, 295, 39, 1,
        0, 0, 0, 296, 299, 3, 60, 30, 0, 297, 299, 3, 46, 23, 0, 298, 296, 1, 0, 0, 0, 298, 297,
        1, 0, 0, 0, 299, 41, 1, 0, 0, 0, 300, 302, 5, 11, 0, 0, 301, 303, 3, 74, 37, 0, 302, 301,
        1, 0, 0, 0, 302, 303, 1, 0, 0, 0, 303, 315, 1, 0, 0, 0, 304, 312, 3, 44, 22, 0, 305, 307,
        5, 4, 0, 0, 306, 308, 3, 74, 37, 0, 307, 306, 1, 0, 0, 0, 307, 308, 1, 0, 0, 0, 308, 309,
        1, 0, 0, 0, 309, 311, 3, 44, 22, 0, 310, 305, 1, 0, 0, 0, 311, 314, 1, 0, 0, 0, 312, 310,
        1, 0, 0, 0, 312, 313, 1, 0, 0, 0, 313, 316, 1, 0, 0, 0, 314, 312, 1, 0, 0, 0, 315, 304,
        1, 0, 0, 0, 315, 316, 1, 0, 0, 0, 316, 318, 1, 0, 0, 0, 317, 319, 3, 74, 37, 0, 318, 317,
        1, 0, 0, 0, 318, 319, 1, 0, 0, 0, 319, 320, 1, 0, 0, 0, 320, 321, 5, 12, 0, 0, 321, 43,
        1, 0, 0, 0, 322, 324, 3, 96, 48, 0, 323, 325, 3, 28, 14, 0, 324, 323, 1, 0, 0, 0, 324,
        325, 1, 0, 0, 0, 325, 326, 1, 0, 0, 0, 326, 327, 5, 1, 0, 0, 327, 330, 3, 94, 47, 0, 328,
        329, 5, 2, 0, 0, 329, 331, 3, 60, 30, 0, 330, 328, 1, 0, 0, 0, 330, 331, 1, 0, 0, 0, 331,
        45, 1, 0, 0, 0, 332, 333, 3, 96, 48, 0, 333, 334, 5, 2, 0, 0, 334, 335, 3, 60, 30, 0, 335,
        47, 1, 0, 0, 0, 336, 353, 3, 96, 48, 0, 337, 340, 5, 6, 0, 0, 338, 341, 5, 54, 0, 0, 339,
        341, 3, 96, 48, 0, 340, 338, 1, 0, 0, 0, 340, 339, 1, 0, 0, 0, 341, 342, 1, 0, 0, 0, 342,
        344, 5, 7, 0, 0, 343, 337, 1, 0, 0, 0, 344, 347, 1, 0, 0, 0, 345, 343, 1, 0, 0, 0, 345,
        346, 1, 0, 0, 0, 346, 354, 1, 0, 0, 0, 347, 345, 1, 0, 0, 0, 348, 351, 5, 13, 0, 0, 349,
        352, 5, 54, 0, 0, 350, 352, 3, 96, 48, 0, 351, 349, 1, 0, 0, 0, 351, 350, 1, 0, 0, 0, 352,
        354, 1, 0, 0, 0, 353, 345, 1, 0, 0, 0, 353, 348, 1, 0, 0, 0, 354, 49, 1, 0, 0, 0, 355, 357,
        5, 6, 0, 0, 356, 358, 3, 74, 37, 0, 357, 356, 1, 0, 0, 0, 357, 358, 1, 0, 0, 0, 358, 370,
        1, 0, 0, 0, 359, 367, 3, 96, 48, 0, 360, 362, 5, 4, 0, 0, 361, 363, 3, 74, 37, 0, 362,
        361, 1, 0, 0, 0, 362, 363, 1, 0, 0, 0, 363, 364, 1, 0, 0, 0, 364, 366, 3, 96, 48, 0, 365,
        360, 1, 0, 0, 0, 366, 369, 1, 0, 0, 0, 367, 365, 1, 0, 0, 0, 367, 368, 1, 0, 0, 0, 368,
        371, 1, 0, 0, 0, 369, 367, 1, 0, 0, 0, 370, 359, 1, 0, 0, 0, 370, 371, 1, 0, 0, 0, 371,
        373, 1, 0, 0, 0, 372, 374, 3, 74, 37, 0, 373, 372, 1, 0, 0, 0, 373, 374, 1, 0, 0, 0, 374,
        375, 1, 0, 0, 0, 375, 376, 5, 7, 0, 0, 376, 51, 1, 0, 0, 0, 377, 379, 5, 11, 0, 0, 378,
        380, 3, 74, 37, 0, 379, 378, 1, 0, 0, 0, 379, 380, 1, 0, 0, 0, 380, 392, 1, 0, 0, 0, 381,
        389, 3, 96, 48, 0, 382, 384, 5, 4, 0, 0, 383, 385, 3, 74, 37, 0, 384, 383, 1, 0, 0, 0,
        384, 385, 1, 0, 0, 0, 385, 386, 1, 0, 0, 0, 386, 388, 3, 96, 48, 0, 387, 382, 1, 0, 0,
        0, 388, 391, 1, 0, 0, 0, 389, 387, 1, 0, 0, 0, 389, 390, 1, 0, 0, 0, 390, 393, 1, 0, 0,
        0, 391, 389, 1, 0, 0, 0, 392, 381, 1, 0, 0, 0, 392, 393, 1, 0, 0, 0, 393, 395, 1, 0, 0,
        0, 394, 396, 3, 74, 37, 0, 395, 394, 1, 0, 0, 0, 395, 396, 1, 0, 0, 0, 396, 397, 1, 0,
        0, 0, 397, 398, 5, 12, 0, 0, 398, 53, 1, 0, 0, 0, 399, 401, 5, 11, 0, 0, 400, 402, 3, 74,
        37, 0, 401, 400, 1, 0, 0, 0, 401, 402, 1, 0, 0, 0, 402, 414, 1, 0, 0, 0, 403, 411, 3, 46,
        23, 0, 404, 406, 5, 4, 0, 0, 405, 407, 3, 74, 37, 0, 406, 405, 1, 0, 0, 0, 406, 407, 1,
        0, 0, 0, 407, 408, 1, 0, 0, 0, 408, 410, 3, 46, 23, 0, 409, 404, 1, 0, 0, 0, 410, 413,
        1, 0, 0, 0, 411, 409, 1, 0, 0, 0, 411, 412, 1, 0, 0, 0, 412, 415, 1, 0, 0, 0, 413, 411,
        1, 0, 0, 0, 414, 403, 1, 0, 0, 0, 414, 415, 1, 0, 0, 0, 415, 417, 1, 0, 0, 0, 416, 418,
        3, 74, 37, 0, 417, 416, 1, 0, 0, 0, 417, 418, 1, 0, 0, 0, 418, 419, 1, 0, 0, 0, 419, 420,
        5, 12, 0, 0, 420, 55, 1, 0, 0, 0, 421, 423, 5, 6, 0, 0, 422, 424, 3, 74, 37, 0, 423, 422,
        1, 0, 0, 0, 423, 424, 1, 0, 0, 0, 424, 436, 1, 0, 0, 0, 425, 433, 3, 60, 30, 0, 426, 428,
        5, 4, 0, 0, 427, 429, 3, 74, 37, 0, 428, 427, 1, 0, 0, 0, 428, 429, 1, 0, 0, 0, 429, 430,
        1, 0, 0, 0, 430, 432, 3, 60, 30, 0, 431, 426, 1, 0, 0, 0, 432, 435, 1, 0, 0, 0, 433, 431,
        1, 0, 0, 0, 433, 434, 1, 0, 0, 0, 434, 437, 1, 0, 0, 0, 435, 433, 1, 0, 0, 0, 436, 425,
        1, 0, 0, 0, 436, 437, 1, 0, 0, 0, 437, 439, 1, 0, 0, 0, 438, 440, 3, 74, 37, 0, 439, 438,
        1, 0, 0, 0, 439, 440, 1, 0, 0, 0, 440, 441, 1, 0, 0, 0, 441, 442, 5, 7, 0, 0, 442, 57, 1,
        0, 0, 0, 443, 445, 5, 11, 0, 0, 444, 446, 3, 2, 1, 0, 445, 444, 1, 0, 0, 0, 445, 446, 1,
        0, 0, 0, 446, 448, 1, 0, 0, 0, 447, 449, 3, 74, 37, 0, 448, 447, 1, 0, 0, 0, 448, 449,
        1, 0, 0, 0, 449, 450, 1, 0, 0, 0, 450, 451, 5, 12, 0, 0, 451, 59, 1, 0, 0, 0, 452, 455,
        3, 62, 31, 0, 453, 454, 5, 17, 0, 0, 454, 456, 3, 82, 41, 0, 455, 453, 1, 0, 0, 0, 455,
        456, 1, 0, 0, 0, 456, 61, 1, 0, 0, 0, 457, 459, 3, 64, 32, 0, 458, 457, 1, 0, 0, 0, 459,
        460, 1, 0, 0, 0, 460, 458, 1, 0, 0, 0, 460, 461, 1, 0, 0, 0, 461, 63, 1, 0, 0, 0, 462, 465,
        3, 66, 33, 0, 463, 465, 3, 68, 34, 0, 464, 462, 1, 0, 0, 0, 464, 463, 1, 0, 0, 0, 465,
        65, 1, 0, 0, 0, 466, 472, 3, 48, 24, 0, 467, 472, 3, 70, 35, 0, 468, 472, 3, 78, 39, 0,
        469, 472, 3, 56, 28, 0, 470, 472, 3, 54, 27, 0, 471, 466, 1, 0, 0, 0, 471, 467, 1, 0,
        0, 0, 471, 468, 1, 0, 0, 0, 471, 469, 1, 0, 0, 0, 471, 470, 1, 0, 0, 0, 472, 474, 1, 0,
        0, 0, 473, 475, 3, 28, 14, 0, 474, 473, 1, 0, 0, 0, 474, 475, 1, 0, 0, 0, 475, 67, 1, 0,
        0, 0, 476, 477, 6, 34, -1, 0, 477, 478, 3, 70, 35, 0, 478, 479, 3, 76, 38, 0, 479, 482,
        1, 0, 0, 0, 480, 482, 3, 66, 33, 0, 481, 476, 1, 0, 0, 0, 481, 480, 1, 0, 0, 0, 482, 488,
        1, 0, 0, 0, 483, 484, 10, 3, 0, 0, 484, 485, 5, 14, 0, 0, 485, 487, 3, 66, 33, 0, 486,
        483, 1, 0, 0, 0, 487, 490, 1, 0, 0, 0, 488, 486, 1, 0, 0, 0, 488, 489, 1, 0, 0, 0, 489,
        69, 1, 0, 0, 0, 490, 488, 1, 0, 0, 0, 491, 493, 3, 96, 48, 0, 492, 494, 3, 34, 17, 0, 493,
        492, 1, 0, 0, 0, 493, 494, 1, 0, 0, 0, 494, 71, 1, 0, 0, 0, 495, 499, 3, 74, 37, 0, 496,
        499, 5, 15, 0, 0, 497, 499, 5, 0, 0, 1, 498, 495, 1, 0, 0, 0, 498, 496, 1, 0, 0, 0, 498,
        497, 1, 0, 0, 0, 499, 73, 1, 0, 0, 0, 500, 502, 5, 47, 0, 0, 501, 500, 1, 0, 0, 0, 502,
        503, 1, 0, 0, 0, 503, 501, 1, 0, 0, 0, 503, 504, 1, 0, 0, 0, 504, 75, 1, 0, 0, 0, 505, 507,
        5, 3, 0, 0, 506, 508, 3, 74, 37, 0, 507, 506, 1, 0, 0, 0, 507, 508, 1, 0, 0, 0, 508, 520,
        1, 0, 0, 0, 509, 517, 3, 40, 20, 0, 510, 512, 5, 4, 0, 0, 511, 513, 3, 74, 37, 0, 512,
        511, 1, 0, 0, 0, 512, 513, 1, 0, 0, 0, 513, 514, 1, 0, 0, 0, 514, 516, 3, 40, 20, 0, 515,
        510, 1, 0, 0, 0, 516, 519, 1, 0, 0, 0, 517, 515, 1, 0, 0, 0, 517, 518, 1, 0, 0, 0, 518,
        521, 1, 0, 0, 0, 519, 517, 1, 0, 0, 0, 520, 509, 1, 0, 0, 0, 520, 521, 1, 0, 0, 0, 521,
        523, 1, 0, 0, 0, 522, 524, 3, 74, 37, 0, 523, 522, 1, 0, 0, 0, 523, 524, 1, 0, 0, 0, 524,
        525, 1, 0, 0, 0, 525, 526, 5, 5, 0, 0, 526, 77, 1, 0, 0, 0, 527, 535, 3, 80, 40, 0, 528,
        535, 5, 51, 0, 0, 529, 535, 5, 48, 0, 0, 530, 535, 5, 52, 0, 0, 531, 535, 5, 30, 0, 0,
        532, 535, 5, 31, 0, 0, 533, 535, 5, 32, 0, 0, 534, 527, 1, 0, 0, 0, 534, 528, 1, 0, 0,
        0, 534, 529, 1, 0, 0, 0, 534, 530, 1, 0, 0, 0, 534, 531, 1, 0, 0, 0, 534, 532, 1, 0, 0,
        0, 534, 533, 1, 0, 0, 0, 535, 79, 1, 0, 0, 0, 536, 538, 7, 1, 0, 0, 537, 539, 5, 50, 0,
        0, 538, 537, 1, 0, 0, 0, 538, 539, 1, 0, 0, 0, 539, 81, 1, 0, 0, 0, 540, 544, 3, 84, 42,
        0, 541, 544, 3, 96, 48, 0, 542, 544, 5, 33, 0, 0, 543, 540, 1, 0, 0, 0, 543, 541, 1, 0,
        0, 0, 543, 542, 1, 0, 0, 0, 544, 83, 1, 0, 0, 0, 545, 553, 5, 34, 0, 0, 546, 553, 5, 35,
        0, 0, 547, 553, 5, 36, 0, 0, 548, 553, 5, 37, 0, 0, 549, 553, 5, 38, 0, 0, 550, 553, 3,
        86, 43, 0, 551, 553, 3, 92, 46, 0, 552, 545, 1, 0, 0, 0, 552, 546, 1, 0, 0, 0, 552, 547,
        1, 0, 0, 0, 552, 548, 1, 0, 0, 0, 552, 549, 1, 0, 0, 0, 552, 550, 1, 0, 0, 0, 552, 551,
        1, 0, 0, 0, 553, 85, 1, 0, 0, 0, 554, 557, 3, 88, 44, 0, 555, 557, 3, 90, 45, 0, 556, 554,
        1, 0, 0, 0, 556, 555, 1, 0, 0, 0, 557, 87, 1, 0, 0, 0, 558, 559, 7, 2, 0, 0, 559, 89, 1,
        0, 0, 0, 560, 565, 5, 42, 0, 0, 561, 562, 5, 9, 0, 0, 562, 563, 3, 88, 44, 0, 563, 564,
        5, 10, 0, 0, 564, 566, 1, 0, 0, 0, 565, 561, 1, 0, 0, 0, 565, 566, 1, 0, 0, 0, 566, 570,
        1, 0, 0, 0, 567, 568, 5, 6, 0, 0, 568, 569, 5, 54, 0, 0, 569, 571, 5, 7, 0, 0, 570, 567,
        1, 0, 0, 0, 570, 571, 1, 0, 0, 0, 571, 588, 1, 0, 0, 0, 572, 577, 5, 43, 0, 0, 573, 574,
        5, 9, 0, 0, 574, 575, 3, 88, 44, 0, 575, 576, 5, 10, 0, 0, 576, 578, 1, 0, 0, 0, 577, 573,
        1, 0, 0, 0, 577, 578, 1, 0, 0, 0, 578, 584, 1, 0, 0, 0, 579, 580, 5, 6, 0, 0, 580, 581,
        5, 54, 0, 0, 581, 583, 5, 7, 0, 0, 582, 579, 1, 0, 0, 0, 583, 586, 1, 0, 0, 0, 584, 582,
        1, 0, 0, 0, 584, 585, 1, 0, 0, 0, 585, 588, 1, 0, 0, 0, 586, 584, 1, 0, 0, 0, 587, 560,
        1, 0, 0, 0, 587, 572, 1, 0, 0, 0, 588, 91, 1, 0, 0, 0, 589, 601, 5, 44, 0, 0, 590, 591,
        5, 9, 0, 0, 591, 596, 3, 94, 47, 0, 592, 593, 5, 4, 0, 0, 593, 595, 3, 94, 47, 0, 594,
        592, 1, 0, 0, 0, 595, 598, 1, 0, 0, 0, 596, 594, 1, 0, 0, 0, 596, 597, 1, 0, 0, 0, 597,
        599, 1, 0, 0, 0, 598, 596, 1, 0, 0, 0, 599, 600, 5, 10, 0, 0, 600, 602, 1, 0, 0, 0, 601,
        590, 1, 0, 0, 0, 601, 602, 1, 0, 0, 0, 602, 606, 1, 0, 0, 0, 603, 604, 5, 6, 0, 0, 604,
        605, 5, 54, 0, 0, 605, 607, 5, 7, 0, 0, 606, 603, 1, 0, 0, 0, 606, 607, 1, 0, 0, 0, 607,
        618, 1, 0, 0, 0, 608, 615, 5, 45, 0, 0, 609, 610, 5, 9, 0, 0, 610, 611, 3, 82, 41, 0, 611,
        612, 5, 4, 0, 0, 612, 613, 3, 94, 47, 0, 613, 614, 5, 10, 0, 0, 614, 616, 1, 0, 0, 0, 615,
        609, 1, 0, 0, 0, 615, 616, 1, 0, 0, 0, 616, 618, 1, 0, 0, 0, 617, 589, 1, 0, 0, 0, 617,
        608, 1, 0, 0, 0, 618, 93, 1, 0, 0, 0, 619, 621, 3, 82, 41, 0, 620, 622, 5, 16, 0, 0, 621,
        620, 1, 0, 0, 0, 621, 622, 1, 0, 0, 0, 622, 95, 1, 0, 0, 0, 623, 624, 5, 49, 0, 0, 624,
        97, 1, 0, 0, 0, 99, 99, 102, 107, 116, 122, 125, 133, 141, 144, 148, 156, 159, 162,
        170, 174, 181, 188, 199, 218, 225, 231, 236, 241, 246, 250, 256, 261, 266, 270,
        276, 281, 286, 289, 292, 298, 302, 307, 312, 315, 318, 324, 330, 340, 345, 351,
        353, 357, 362, 367, 370, 373, 379, 384, 389, 392, 395, 401, 406, 411, 414, 417,
        423, 428, 433, 436, 439, 445, 448, 455, 460, 464, 471, 474, 481, 488, 493, 498,
        503, 507, 512, 517, 520, 523, 534, 538, 543, 552, 556, 565, 570, 577, 584, 587,
        596, 601, 606, 615, 617, 621
    ]


class PslParser(Parser):
    grammarFileName = "Psl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "':'", "'='", "'('", "','", "')'", "'['",
                    "']'", "'@'", "'<'", "'>'", "'{'", "'}'", "'.'", "'->'",
                    "';'", "'?'", "'as'", "'let'", "'use'", "'func'", "'type'",
                    "'enum'", "'with'", "'return'", "'inner'", "'sync'",
                    "'scoped'", "'static'", "'atomic'", "'null'", "'true'",
                    "'false'", "'any'", "'number'", "'string'", "'bool'",
                    "'functor'", "'block'", "'int'", "'real'", "'complex'",
                    "'array'", "'matrix'", "'list'", "'dict'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "AS", "LET", "USE", "FUNC", "TYPE", "ENUM",
                     "WITH", "RETURN", "INNER", "SYNC", "SCOPED", "STATIC",
                     "ATOMIC", "NULL", "TRUE", "FALSE", "ANY_TYPE", "NUMBER_TYPE",
                     "STRING_TYPE", "BOOLEAN_TYPE", "FUNCTOR_TYPE", "BLOCK_TYPE",
                     "INTEGER_TYPE", "REAL_TYPE", "COMPLEX_TYPE", "ARRAY_TYPE",
                     "MATRIX_TYPE", "LIST_TYPE", "DICT_TYPE", "SKIP_",
                     "LINE_END", "MULTI_STR", "IDENTIFIER", "UNIT", "STRING",
                     "FSTRING", "COMPLEX", "INTEGER", "REAL", "DECIMAL_INTEGER"]

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
    RULE_vectorType = 45
    RULE_structType = 46
    RULE_nullableType = 47
    RULE_identRef = 48

    ruleNames = ["program", "stmtList", "stmt", "letStmt", "useStmt",
                 "withDef", "funcDef", "typeDef", "enumDef", "retStmt",
                 "exprStmt", "carrier", "biasAnno", "sizeAnno", "annotation",
                 "annotations", "modifiers", "withList", "withDecl", "paramDef",
                 "argument", "typePack", "keyValDecl", "keyValExpr", "entityRef",
                 "listUnpack", "dictUnpack", "dictPack", "listPack", "stmtPack",
                 "entityExpr", "entityChain", "chainUnit", "entity", "linkCall",
                 "functorRef", "stmtEnd", "sepMark", "argsList", "literal",
                 "value", "type", "innerType", "numberType", "scalarType",
                 "vectorType", "structType", "nullableType", "identRef"]

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
    AS = 17
    LET = 18
    USE = 19
    FUNC = 20
    TYPE = 21
    ENUM = 22
    WITH = 23
    RETURN = 24
    INNER = 25
    SYNC = 26
    SCOPED = 27
    STATIC = 28
    ATOMIC = 29
    NULL = 30
    TRUE = 31
    FALSE = 32
    ANY_TYPE = 33
    NUMBER_TYPE = 34
    STRING_TYPE = 35
    BOOLEAN_TYPE = 36
    FUNCTOR_TYPE = 37
    BLOCK_TYPE = 38
    INTEGER_TYPE = 39
    REAL_TYPE = 40
    COMPLEX_TYPE = 41
    ARRAY_TYPE = 42
    MATRIX_TYPE = 43
    LIST_TYPE = 44
    DICT_TYPE = 45
    SKIP_ = 46
    LINE_END = 47
    MULTI_STR = 48
    IDENTIFIER = 49
    UNIT = 50
    STRING = 51
    FSTRING = 52
    COMPLEX = 53
    INTEGER = 54
    REAL = 55
    DECIMAL_INTEGER = 56

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
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70790965232404800) != 0):
                self.state = 98
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
            self.state = 105
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 101
                        self.sepMark()

                    self.state = 104
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 107
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
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.letStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.useStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.funcDef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.typeDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.enumDef()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.retStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 115
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
            self.state = 118
            self.match(PslParser.LET)
            self.state = 119
            self.carrier()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 1:
                self.state = 120
                self.match(PslParser.T__0)
                self.state = 121
                self.type_()

            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 124
                self.match(PslParser.T__1)

            self.state = 127
            self.entityExpr()
            self.state = 128
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
            self.state = 130
            self.match(PslParser.USE)
            self.state = 131
            self.carrier()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 132
                self.match(PslParser.T__1)

            self.state = 135
            self.entityExpr()
            self.state = 136
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
            self.state = 138
            self.match(PslParser.WITH)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.state = 139
                self.identRef()
                pass
            elif token in [9]:
                self.state = 140
                self.withDecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 143
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
            self.state = 146
            self.annotations()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 23:
                self.state = 147
                self.withDef()

            self.state = 150
            self.modifiers()
            self.state = 151
            self.match(PslParser.FUNC)
            self.state = 152
            self.identRef()
            self.state = 153
            self.paramDef()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 1:
                self.state = 154
                self.match(PslParser.T__0)
                self.state = 155
                self.type_()

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 158
                self.match(PslParser.T__1)

            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 161
                self.match(PslParser.LINE_END)

            self.state = 164
            self.stmtPack()
            self.state = 165
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
            self.state = 167
            self.match(PslParser.TYPE)
            self.state = 168
            self.identRef()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 169
                self.match(PslParser.T__1)

            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 49]:
                self.state = 172
                self.type_()
                pass
            elif token in [11]:
                self.state = 173
                self.typePack()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 176
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
            self.state = 178
            self.match(PslParser.ENUM)
            self.state = 179
            self.identRef()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 180
                self.match(PslParser.T__1)

            self.state = 183
            self.dictUnpack()
            self.state = 184
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
            self.state = 186
            self.match(PslParser.RETURN)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70650226670569536) != 0):
                self.state = 187
                self.entityExpr()

            self.state = 190
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
            self.state = 192
            self.annotations()
            self.state = 193
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
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.entityRef()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.listUnpack()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
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
            self.state = 201
            self.match(PslParser.T__2)
            self.state = 202
            self.match(PslParser.INTEGER)
            self.state = 203
            self.match(PslParser.T__3)
            self.state = 204
            self.match(PslParser.INTEGER)
            self.state = 205
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
            self.state = 207
            self.match(PslParser.T__5)
            self.state = 208
            self.match(PslParser.INTEGER)
            self.state = 209
            self.match(PslParser.T__3)
            self.state = 210
            self.match(PslParser.INTEGER)
            self.state = 211
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
            self.state = 213
            self.match(PslParser.T__7)
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.state = 214
                self.identRef()
                pass
            elif token in [11]:
                self.state = 215
                self.dictPack()
                pass
            elif token in [3]:
                self.state = 216
                self.biasAnno()
                pass
            elif token in [6]:
                self.state = 217
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
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 8:
                self.state = 220
                self.annotation()
                self.state = 221
                self.match(PslParser.LINE_END)
                self.state = 227
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
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0):
                self.state = 228
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 233
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
            self.state = 234
            self.match(PslParser.T__8)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 235
                self.sepMark()

            self.state = 238
            self.argument()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 239
                self.match(PslParser.T__3)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 47:
                    self.state = 240
                    self.sepMark()

                self.state = 243
                self.argument()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 249
                self.sepMark()

            self.state = 252
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
            self.state = 254
            self.match(PslParser.T__8)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 255
                self.sepMark()

            self.state = 258
            self.keyValDecl()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 259
                self.match(PslParser.T__3)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 47:
                    self.state = 260
                    self.sepMark()

                self.state = 263
                self.keyValDecl()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 269
                self.sepMark()

            self.state = 272
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
            self.state = 274
            self.match(PslParser.T__2)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 29, self._ctx)
            if la_ == 1:
                self.state = 275
                self.sepMark()

            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 49:
                self.state = 278
                self.keyValDecl()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 279
                    self.match(PslParser.T__3)
                    self.state = 281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 280
                        self.sepMark()

                    self.state = 283
                    self.keyValDecl()
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 291
                self.sepMark()

            self.state = 294
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
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 34, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.entityExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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
            self.state = 300
            self.match(PslParser.T__10)
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 35, self._ctx)
            if la_ == 1:
                self.state = 301
                self.sepMark()

            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 49:
                self.state = 304
                self.keyValDecl()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 305
                    self.match(PslParser.T__3)
                    self.state = 307
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 306
                        self.sepMark()

                    self.state = 309
                    self.keyValDecl()
                    self.state = 314
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 317
                self.sepMark()

            self.state = 320
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
            self.state = 322
            self.identRef()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 8:
                self.state = 323
                self.annotation()

            self.state = 326
            self.match(PslParser.T__0)
            self.state = 327
            self.nullableType()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 2:
                self.state = 328
                self.match(PslParser.T__1)
                self.state = 329
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
            self.state = 332
            self.identRef()
            self.state = 333
            self.match(PslParser.T__1)
            self.state = 334
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
            self.state = 336
            self.identRef()
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 45, self._ctx)
            if la_ == 1:
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 43, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 337
                        self.match(PslParser.T__5)
                        self.state = 340
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [54]:
                            self.state = 338
                            self.match(PslParser.INTEGER)
                            pass
                        elif token in [49]:
                            self.state = 339
                            self.identRef()
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 342
                        self.match(PslParser.T__6)
                    self.state = 347
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 43, self._ctx)

                pass

            elif la_ == 2:
                self.state = 348
                self.match(PslParser.T__12)
                self.state = 351
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [54]:
                    self.state = 349
                    self.match(PslParser.INTEGER)
                    pass
                elif token in [49]:
                    self.state = 350
                    self.identRef()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


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
            self.state = 355
            self.match(PslParser.T__5)
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 46, self._ctx)
            if la_ == 1:
                self.state = 356
                self.sepMark()

            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 49:
                self.state = 359
                self.identRef()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 360
                    self.match(PslParser.T__3)
                    self.state = 362
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 361
                        self.sepMark()

                    self.state = 364
                    self.identRef()
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 372
                self.sepMark()

            self.state = 375
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
            self.state = 377
            self.match(PslParser.T__10)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 51, self._ctx)
            if la_ == 1:
                self.state = 378
                self.sepMark()

            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 49:
                self.state = 381
                self.identRef()
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 382
                    self.match(PslParser.T__3)
                    self.state = 384
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 383
                        self.sepMark()

                    self.state = 386
                    self.identRef()
                    self.state = 391
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 394
                self.sepMark()

            self.state = 397
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
            self.state = 399
            self.match(PslParser.T__10)
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 56, self._ctx)
            if la_ == 1:
                self.state = 400
                self.sepMark()

            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 49:
                self.state = 403
                self.keyValExpr()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 404
                    self.match(PslParser.T__3)
                    self.state = 406
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 405
                        self.sepMark()

                    self.state = 408
                    self.keyValExpr()
                    self.state = 413
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 416
                self.sepMark()

            self.state = 419
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
            self.state = 421
            self.match(PslParser.T__5)
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 61, self._ctx)
            if la_ == 1:
                self.state = 422
                self.sepMark()

            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70650226670569536) != 0):
                self.state = 425
                self.entityExpr()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 426
                    self.match(PslParser.T__3)
                    self.state = 428
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 427
                        self.sepMark()

                    self.state = 430
                    self.entityExpr()
                    self.state = 435
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 438
                self.sepMark()

            self.state = 441
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
            self.state = 443
            self.match(PslParser.T__10)
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 66, self._ctx)
            if la_ == 1:
                self.state = 444
                self.stmtList()

            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 447
                self.sepMark()

            self.state = 450
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
            self.state = 452
            self.entityChain()
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 17:
                self.state = 453
                self.match(PslParser.AS)
                self.state = 454
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
            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 457
                self.chainUnit()
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70650226670569536) != 0)):
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
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 70, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
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
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 71, self._ctx)
            if la_ == 1:
                self.state = 466
                self.entityRef()
                pass

            elif la_ == 2:
                self.state = 467
                self.functorRef()
                pass

            elif la_ == 3:
                self.state = 468
                self.literal()
                pass

            elif la_ == 4:
                self.state = 469
                self.listPack()
                pass

            elif la_ == 5:
                self.state = 470
                self.dictPack()
                pass

            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 72, self._ctx)
            if la_ == 1:
                self.state = 473
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
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 73, self._ctx)
            if la_ == 1:
                self.state = 477
                self.functorRef()
                self.state = 478
                self.argsList()
                pass

            elif la_ == 2:
                self.state = 480
                self.entity()
                pass

            self._ctx.stop = self._input.LT(-1)
            self.state = 488
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 74, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PslParser.LinkCallContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_linkCall)
                    self.state = 483
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 484
                    self.match(PslParser.T__13)
                    self.state = 485
                    self.entity()
                self.state = 490
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 74, self._ctx)

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
            self.state = 491
            self.identRef()
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 75, self._ctx)
            if la_ == 1:
                self.state = 492
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
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.sepMark()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
                self.match(PslParser.T__14)
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 497
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
            self.state = 501
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 500
                    self.match(PslParser.LINE_END)

                else:
                    raise NoViableAltException(self)
                self.state = 503
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 77, self._ctx)

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
            self.state = 505
            self.match(PslParser.T__2)
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 78, self._ctx)
            if la_ == 1:
                self.state = 506
                self.sepMark()

            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70650226670569536) != 0):
                self.state = 509
                self.argument()
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 510
                    self.match(PslParser.T__3)
                    self.state = 512
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == 47:
                        self.state = 511
                        self.sepMark()

                    self.state = 514
                    self.argument()
                    self.state = 519
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 47:
                self.state = 522
                self.sepMark()

            self.state = 525
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
            self.state = 534
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53, 54, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.value()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
                self.match(PslParser.STRING)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 529
                self.match(PslParser.MULTI_STR)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 4)
                self.state = 530
                self.match(PslParser.FSTRING)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 531
                self.match(PslParser.NULL)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 6)
                self.state = 532
                self.match(PslParser.TRUE)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 7)
                self.state = 533
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

        def COMPLEX(self):
            return self.getToken(PslParser.COMPLEX, 0)

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
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 63050394783186944) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 84, self._ctx)
            if la_ == 1:
                self.state = 537
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
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.innerType()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.identRef()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 542
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
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.match(PslParser.NUMBER_TYPE)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.match(PslParser.STRING_TYPE)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 547
                self.match(PslParser.BOOLEAN_TYPE)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 548
                self.match(PslParser.FUNCTOR_TYPE)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 549
                self.match(PslParser.BLOCK_TYPE)
                pass
            elif token in [39, 40, 41, 42, 43]:
                self.enterOuterAlt(localctx, 6)
                self.state = 550
                self.numberType()
                pass
            elif token in [44, 45]:
                self.enterOuterAlt(localctx, 7)
                self.state = 551
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
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.scalarType()
                pass
            elif token in [42, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
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
            self.state = 558
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
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
        self.enterRule(localctx, 90, self.RULE_vectorType)
        self._la = 0  # Token type
        try:
            self.state = 587
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.match(PslParser.ARRAY_TYPE)
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 561
                    self.match(PslParser.T__8)
                    self.state = 562
                    self.scalarType()
                    self.state = 563
                    self.match(PslParser.T__9)

                self.state = 570
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 89, self._ctx)
                if la_ == 1:
                    self.state = 567
                    self.match(PslParser.T__5)
                    self.state = 568
                    self.match(PslParser.INTEGER)
                    self.state = 569
                    self.match(PslParser.T__6)

                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
                self.match(PslParser.MATRIX_TYPE)
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 573
                    self.match(PslParser.T__8)
                    self.state = 574
                    self.scalarType()
                    self.state = 575
                    self.match(PslParser.T__9)

                self.state = 584
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 91, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 579
                        self.match(PslParser.T__5)
                        self.state = 580
                        self.match(PslParser.INTEGER)
                        self.state = 581
                        self.match(PslParser.T__6)
                    self.state = 586
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
        self.enterRule(localctx, 92, self.RULE_structType)
        self._la = 0  # Token type
        try:
            self.state = 617
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.match(PslParser.LIST_TYPE)
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 590
                    self.match(PslParser.T__8)
                    self.state = 591
                    self.nullableType()
                    self.state = 596
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == 4:
                        self.state = 592
                        self.match(PslParser.T__3)
                        self.state = 593
                        self.nullableType()
                        self.state = 598
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 599
                    self.match(PslParser.T__9)

                self.state = 606
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 95, self._ctx)
                if la_ == 1:
                    self.state = 603
                    self.match(PslParser.T__5)
                    self.state = 604
                    self.match(PslParser.INTEGER)
                    self.state = 605
                    self.match(PslParser.T__6)

                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.match(PslParser.DICT_TYPE)
                self.state = 615
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 9:
                    self.state = 609
                    self.match(PslParser.T__8)
                    self.state = 610
                    self.type_()
                    self.state = 611
                    self.match(PslParser.T__3)
                    self.state = 612
                    self.nullableType()
                    self.state = 613
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
        self.enterRule(localctx, 94, self.RULE_nullableType)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.type_()
            self.state = 621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 16:
                self.state = 620
                self.match(PslParser.T__15)


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
        self.enterRule(localctx, 96, self.RULE_identRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
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
