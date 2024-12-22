import asyncio
import random
import sys

async def merge(A, B, start, middle, finish, ev_in1, ev_in2, ev_out):
    await ev_in1.wait()
    if middle < finish: await ev_in2.wait()
    i, j, k = start, middle, start
    while i < middle and j < finish:
        B[k] = A[i] if A[i] <= A[j] else A[j]
        i, j = i + 1 if A[i] <= A[j] else i, j + 1 if A[i] > A[j] else j
        k += 1
    while i < middle: B[k], i, k = A[i], i + 1, k + 1
    while j < finish: B[k], j, k = A[j], j + 1, k + 1
    ev_out.set()

async def mtasks(A):
    N = len(A)
    evs, B, tasks = [asyncio.Event() for _ in range(N)], [0] * N, []
    for ev in evs: ev.set()
    step, src, dst = 1, A.copy(), B
    while step < N:
        next_evs = [asyncio.Event() for _ in range((N + 2 * step - 1) // (2 * step))]
        for i in range(0, N, 2 * step):
            tasks.append(asyncio.create_task(merge(
                src, dst, i, min(i + step, N), min(i + 2 * step, N),
                evs[i // step], evs[min(i + step, N) // step] if min(i + step, N) < N else asyncio.Event(),
                next_evs[i // (2 * step)]
            )))
        evs, src, dst = next_evs, dst, src
        step *= 2
    return tasks, src

exec(sys.stdin.read())
