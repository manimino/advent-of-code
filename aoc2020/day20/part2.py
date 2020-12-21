import numpy as np

part1_grid = [
    ['2897_f1r1', '1777_f1r1', '3121_f0r3', '3371_f1r3', '3301_f1r1', '1301_f1r1', '2521_f0r1', '3463_f0r3', '2551_f0r0', '1427_f1r1', '1861_f1r0', '1439_f1r0'],
    ['2459_f0r3', '1201_f0r0', '1063_f0r3', '2441_f1r1', '3329_f1r0', '3701_f0r3', '2707_f0r1', '3491_f0r1', '2531_f0r3', '2027_f0r1', '3347_f1r2', '1607_f0r1'],
    ['1721_f0r3', '2777_f1r2', '1231_f0r3', '2579_f0r3', '2819_f1r2', '3709_f0r3', '2663_f1r0', '3673_f1r3', '1559_f0r1', '1031_f1r3', '3823_f0r0', '2969_f1r1'],
    ['1663_f1r3', '2053_f0r3', '2917_f0r3', '3169_f1r3', '1103_f1r1', '1831_f1r3', '3041_f0r3', '3697_f0r1', '1987_f0r0', '3433_f1r1', '2887_f1r3', '3343_f1r1'],
    ['3779_f0r3', '3929_f1r1', '2039_f1r2', '3769_f0r0', '2879_f1r2', '2081_f1r3', '2971_f1r3', '2503_f0r3', '1753_f0r1', '2539_f0r0', '3137_f1r0', '2017_f1r2'],
    ['1627_f1r1', '2857_f1r2', '3359_f0r1', '1123_f0r0', '3739_f0r0', '3313_f1r3', '3023_f1r1', '1549_f1r1', '2797_f0r1', '2141_f0r0', '3191_f1r1', '2399_f0r3'],
    ['1823_f1r2', '1801_f0r1', '2803_f0r1', '1637_f1r2', '3229_f1r3', '2063_f0r0', '3989_f1r1', '3527_f0r0', '2153_f1r0', '3719_f0r1', '1907_f1r1', '1429_f0r1'],
    ['1483_f0r0', '2347_f1r3', '1433_f0r1', '2557_f1r2', '1709_f1r2', '3061_f1r1', '1471_f1r0', '1901_f1r0', '2267_f1r1', '2671_f1r1', '1303_f1r0', '3853_f1r0'],
    ['1019_f0r0', '2939_f1r1', '1787_f0r0', '3541_f1r0', '2069_f1r3', '3011_f1r1', '1327_f0r3', '3539_f0r1', '2801_f0r0', '2843_f1r3', '2411_f0r1', '3407_f1r3'],
    ['1747_f0r0', '1249_f1r0', '3517_f1r3', '3877_f1r1', '2749_f1r3', '2687_f1r1', '1999_f1r2', '2957_f0r0', '1447_f0r3', '3323_f0r1', '1933_f0r1', '1583_f0r0'],
    ['3257_f1r1', '2659_f1r2', '2543_f1r0', '2083_f1r0', '2423_f1r0', '1511_f1r0', '1297_f0r1', '2251_f0r0', '3793_f1r1', '3221_f0r3', '3083_f1r3', '1109_f1r1'],
    ['1453_f1r0', '1291_f0r1', '1951_f1r0', '2137_f0r0', '1997_f1r0', '1609_f1r3', '2131_f0r3', '1867_f1r3', '1187_f1r0', '3917_f1r3', '2689_f1r3', '2477_f0r1']
]

part1_grid_test = [
    ['2971_f0r0', '1489_f0r0', '1171_f0r2'],
    ['2729_f0r0', '1427_f0r0', '2473_f0r1'],
    ['1951_f0r0', '2311_f0r0', '3079_f1r2']
]

INPUT = ('input.txt', part1_grid)
TEST_INPUT = ('test_input.txt', part1_grid_test)

USING = INPUT


def img_from_strings(str_list):
    # prints a numpy array of strings as a picture
    arrs = []
    sz = None
    for line in str_list:
        if line.strip():
            if sz is None:
                sz = len(line.strip())
            elif len(line.strip()) != sz:
                raise Exception('size mismatch, check input')
            arrs.append(list(line))
    return np.array(arrs)


def get_nessie_coords():
    NESSIE = \
"""
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
""".replace(' ', '.')
    base_nessie = img_from_strings(NESSIE.split('\n'))
    flip_nessie = np.fliplr(base_nessie)
    nessies = []
    for n in [base_nessie, flip_nessie]:
        for _ in range(4):
            n = np.rot90(n)
            rs, cs = np.where(n == '#')
            rcs = list(zip(rs, cs))
            nessies.append(rcs)
    return nessies


def read_input_objs():
    # for puzzles with newline-separated objects as input
    with open(USING[0]) as fh:
        obj = []
        num = None
        for line in fh.readlines():
            if not line.strip():
                yield num, img_from_strings(obj)
                obj = []
            else:
                if line.startswith('Tile'):
                    # first line is Tile: num
                    num_str = line.strip().split(' ')[1]
                    num = num_str.replace(':', '')
                else:
                    obj.append(line.strip())
        if obj:
            yield num, img_from_strings(obj)


def cut_off_edges(img):
    # "img" is a 2D numpy array of char
    return img[1:-1, 1:-1]


def print_img(img):
    # "img" is a 2D numpy array of char
    nrows, ncols = img.shape
    for r in range(nrows):
        print(''.join(list(img[r,:])))



def get_img():
    tiles = {}
    for num, tile in read_input_objs():
        tiles[num] = cut_off_edges(tile)
    grid = USING[1]
    grid_img_data = None
    for r in range(len(grid)):
        grid_img_data_row = None
        for c in range(len(grid[r])):
            tile_info = grid[r][c]
            tnum, tform = tile_info.split('_')
            to_flip = tform[1]
            to_rot = tform[3]
            tile = tiles[tnum]
            if to_flip == '1':
                tile = np.fliplr(tile)
            for _ in range(4-int(to_rot)):
                tile = np.rot90(tile)
            if grid_img_data_row is None:
                grid_img_data_row = tile
            else:
                grid_img_data_row = np.concatenate((grid_img_data_row, tile), axis=1)
        if grid_img_data is None:
            grid_img_data = grid_img_data_row
        else:
            grid_img_data = np.concatenate((grid_img_data, grid_img_data_row), axis=0)
    return grid_img_data


def tag_nessies(img, nessie_rc):
    rows, cols = img.shape
    max_offset_r = max(rc[0] for rc in nessie_rc)
    max_offset_c = max(rc[1] for rc in nessie_rc)
    rmax = rows - max_offset_r
    cmax = cols - max_offset_c

    for r in range(rmax):
        for c in range(cmax):
            spotted = True
            for nrc in nessie_rc:
                if img[r+nrc[0], c+nrc[1]] == '.':
                    spotted = False
                    break
            if spotted:
                for nrc in nessie_rc:
                    img[r+nrc[0], c+nrc[1]] = 'O'


def count_hashes(img):
    rs, cs = np.where(img=='#')
    return len(rs)


def main():
    img = get_img()
    nessie_rcs = get_nessie_coords()

    print_img(np.flipud(img))
    for n in nessie_rcs:
        tag_nessies(img, n)

    print(count_hashes(img))

if __name__ == '__main__':
    main()
    # 2020 too high

"""
#.###.....#.##...######.
.O##.#OO.##..#....#####.
..O#.O..O####.#.####.###
                   # 
 #    ##    ##    ###
  #  #  #  #  #  #   
"""