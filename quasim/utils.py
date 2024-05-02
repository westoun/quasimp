#!/usr/bin/env python3

from dataclasses import dataclass
import math
import numpy as np
from typing import List
import warnings


@dataclass
class QubitGroup:
    qubits: List[int]
    state: np.ndarray


def probabilities_from_state(state: np.ndarray) -> np.ndarray:
    conjugate = state.conjugate()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        # Ignore "np.complex128Warning: Casting np.complex128 values to real discards the imaginary part"
        # since that is precisely what we want.
        probabilities = np.multiply(state, conjugate).astype(float)

    return probabilities


def probability_dict_from_state(state: np.ndarray) -> np.ndarray:
    qubit_num = int(math.log2(len(state)))

    probabilities = probabilities_from_state(state)

    probability_dict = {}
    for i, probability in enumerate(probabilities):

        if probability == 0:
            continue

        state: str = ""

        remainder = i
        for j in reversed(range(qubit_num)):

            if remainder >= 2**j:
                state += "1"
                remainder -= 2**j
            else:
                state += "0"

        probability_dict[state] = probability

    return probability_dict