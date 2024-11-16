import pandas as pd
import numpy as np

def get_positions(pos_dict):
    pos = pd.Series(pos_dict)
    pos = pos.replace([np.inf, -np.inf], np.nan)
    pos = pos.dropna()
    pos = pos / pos.abs().sum()
    pos = pos.clip(-0.1, 0.1)
    if pos.abs().max() / pos.abs().sum() > 0.1:
        raise ValueError(
            f"Portfolio too concentrated {pos.abs().max()=} / {pos.abs().sum()=}"
        )
    return pos


def get_submission_dict(
    pos_dict,
    your_team_name: str = "a_great_team_name",
    your_team_passcode: str = "a_strong_p4$$c0d3",
):

    return {
        **get_positions(pos_dict).to_dict(),
        **{
            "team_name": your_team_name,
            "passcode": your_team_passcode,
        },
    }


get_submission_dict(
    {
        **{f"strat_{i}": 0.1 for i in range(10)},
        "strat_bad": np.nan,
        "strat_bad2": -np.inf,
    }
)
