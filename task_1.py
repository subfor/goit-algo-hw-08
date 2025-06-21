import heapq


def minimal_connection_plan(cables):
    heapq.heapify(cables)
    total_cost = 0
    steps = []

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second

        # Зберігаємо порядок з'єднання
        steps.append((first, second, cost))

        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost, steps


def main():
    cables = [8, 4, 6, 12]
    total, steps = minimal_connection_plan(cables)

    print("Загальні витрати:", total)
    print("Порядок об'єднань:")
    for step in steps:
        print(f"{step[0]} + {step[1]} = {step[2]}")


if __name__ == "__main__":
    main()
