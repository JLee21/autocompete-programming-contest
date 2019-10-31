import fileinput

"""
Example Input
ball <0,0>
hole <15,20>
<5,5>
<7,5>
<3,8>
<0,2>
<1,1>
<-2,1>
"""


def parse_two_nums(coord_str):
    #  "<15,20>"
    coord_str = coord_str.split()[-1]
    num_str = coord_str[1:-1].split(",")  # "15", "20"
    nums = list(map(int, num_str))
    return nums


line_num = 0
hit = 0
for line in fileinput.input():

    if line_num == 0:
        # Save the hole position
        ball_pos = parse_two_nums(line)

    if line_num == 1:
        # Save the starting position
        hole_pos = parse_two_nums(line)

    line_num += 1

    if line_num > 2:
        # Add hit value
        hit_vals = parse_two_nums(line)  # [5, 5]
        ball_pos[0] += hit_vals[0]  # x
        ball_pos[1] += hit_vals[1]  # x
        hit += 1

        # check if in hole
        if ball_pos == hole_pos:
            print('Hole in {}'.format(hit))
            exit()


print("Ball did not make the hole -\_**_/-")
