def dr_keys() -> None:
    vr("d").move(y=15)
    vr("d").nwrite("-" * 52)
    kseq = None
    if not vr("caps"):
        kseq = "|  esc  `  1  2  3  4  5  6  7  8  9  0  -  =  bck ||"
    elif vr("caps") == 2:
        kseq = "|  ESC  ~  1  2  3  4  5  6  7  8  9  0  _  +  BCK ||"
    else:
        kseq = "|  ESC  ~  !  @  #  $  %  ^  &  *  (  )  _  +  BCK ||"
    if not vr("caps"):
        kseq += str(
            " " * 2
            + "tab     q  w  e  r  t  y  u  i  o  p  [  ]   \\  ||"
            + " " * 2
            + "caps    a  s  d  f  g  h  j  k  l  ;   '  enter ||"
            + " " * 2
            + "shift   z  x  c  v  b  n  m  ,  .   /   space <<"
        )
    else:
        capsl = "caps"
        if vr("caps") == 2:
            capsl = capsl.upper()
        kseq += str(
            " " * 2
            + "TAB     Q  W  E  R  T  Y  U  I  O  P  {  }   |  ||"
            + " " * 2
            + capsl
            + '    A  S  D  F  G  H  J  K  L  :   "  ENTER ||'
            + " " * 2
            + "SHIFT   Z  X  C  V  B  N  M  <  >   ?   SPACE <<"
        )
    vr("d").nwrite(kseq)


vr("dr_keys", dr_keys)
del dr_keys

vr(
    "vkloc",
    [
        [0, 3, 7],
        [0, 8, 10],
        [0, 11, 13],
        [0, 14, 16],
        [0, 17, 19],
        [0, 20, 22],
        [0, 23, 25],
        [0, 26, 28],
        [0, 29, 31],
        [0, 32, 34],
        [0, 35, 37],
        [0, 38, 40],
        [0, 41, 43],
        [0, 44, 46],
        [0, 47, 51],
        [1, 3, 7],
        [1, 11, 13],
        [1, 14, 16],
        [1, 17, 19],
        [1, 20, 22],
        [1, 23, 25],
        [1, 26, 28],
        [1, 29, 31],
        [1, 32, 34],
        [1, 35, 37],
        [1, 38, 40],
        [1, 41, 43],
        [1, 44, 46],
        [1, 48, 50],
        [2, 3, 8],
        [2, 11, 13],
        [2, 14, 16],
        [2, 17, 19],
        [2, 20, 22],
        [2, 23, 25],
        [2, 26, 28],
        [2, 29, 31],
        [2, 32, 34],
        [2, 35, 37],
        [2, 38, 40],
        [2, 42, 44],
        [2, 45, 51],
        [3, 3, 9],
        [3, 11, 13],
        [3, 14, 16],
        [3, 17, 19],
        [3, 20, 22],
        [3, 23, 25],
        [3, 26, 28],
        [3, 29, 31],
        [3, 32, 34],
        [3, 35, 37],
        [3, 39, 41],
        [3, 43, 49],
    ],
)

vr(
    "keys",
    [
        [-1, -1],
        [96, 126],
        [49, 33],
        [50, 64],
        [51, 35],
        [52, 36],
        [53, 37],
        [54, 94],
        [55, 38],
        [56, 42],
        [57, 40],
        [48, 41],
        [45, 95],
        [61, 43],
        [127, 127],
        [9, 9],
        [113, 81],
        [119, 87],
        [101, 69],
        [114, 82],
        [116, 84],
        [121, 89],
        [117, 85],
        [105, 73],
        [111, 79],
        [112, 80],
        [91, 123],
        [93, 125],
        [92, 124],
        [400, 400],
        [97, 65],
        [115, 83],
        [100, 68],
        [102, 70],
        [103, 71],
        [104, 72],
        [106, 74],
        [107, 75],
        [108, 76],
        [59, 58],
        [39, 34],
        [10, 10],
        [401, 401],
        [122, 90],
        [120, 88],
        [99, 67],
        [118, 86],
        [98, 66],
        [110, 78],
        [109, 77],
        [44, 60],
        [46, 62],
        [47, 63],
        [32, 32],
    ],
)
vrp("ok")