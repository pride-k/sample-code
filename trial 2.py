piece_type = input("Enter the piece type: ").lower()
row = int(input("Enter the row starting position (1-8): "))
col = int(input("Enter the column starting position (1-8): "))
valid_movements = {"left":[],"right":[],"forward":[],"backward":[],"left forward diagonal":[],"right forward diagonal":[],"left backward diagonal":[],"right backward diagonal":[]}
directions = {
    "king": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
    "queen": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
    "bishop": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    "rook": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "pawn": [(1, 0), (1, -1), (1, 1)],
}
if piece_type not in directions:
    print("Invalid piece type.")
else:
    for dr, dc in directions[piece_type]:
        r, c = row, col
        for _ in range(1, 8):
            r += dr
            c += dc
            if 1 <= r <= 8 and 1 <= c <= 8:
                if dr == 0 and dc == -1:
                    valid_movements["left"].append((r, c))
                elif dr == 0 and dc == 1:
                    valid_movements["right"].append((r, c))
                elif dr == 1 and dc == 0:
                    valid_movements["forward"].append((r, c))
                elif dr == -1 and dc == 0:
                    valid_movements["backward"].append((r, c))
                elif dr == 1 and dc == -1:
                    valid_movements["left forward diagonal"].append((r, c))
                elif dr == 1 and dc == 1:
                    valid_movements["right forward diagonal"].append((r, c))
                elif dr == -1 and dc == -1:
                    valid_movements["left backward diagonal"].append((r, c))
                elif dr == -1 and dc == 1:
                    valid_movements["right backward diagonal"].append((r, c))
            else:
                break
    for direction, movements in valid_movements.items():
        print(f"{direction}: {str(movements).replace('[','').replace(']','').replace(' ','')}")