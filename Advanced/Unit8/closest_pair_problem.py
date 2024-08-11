def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def closest_pair(points):
    if len(points) <= 3:
        return min([distance(p1, p2) for p1 in points for p2 in points if p1 != p2])

    mid = len(points) // 2
    median = sorted(points, key=lambda x: x[0])[mid][0]

    left_half = [p for p in points if p[0] <= median]
    right_half = [p for p in points if p[0] > median]

    d_left = closest_pair(left_half)
    d_right = closest_pair(right_half)

    d = min(d_left, d_right)

    strip = [p for p in left_half if distance((median, 0), p) < d]
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip) - 1):
        for j in range(i + 1, min(i + 4, len(strip))):
            d = distance(strip[i], strip[j])
            if d < d_left:
                d_left = d

    return d_left