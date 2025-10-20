# Super Bowl Data Analysis

Exploratory analysis of Super Bowl history using Python + Pandas.  
Dataset includes winner/loser, points, MVP, stadium/city/state.

## Dataset
- Source: Kaggle — Super Bowl History
- File: `superbowl.csv`

## Questions explored
- Which teams win most often?
- What winning scores occur most frequently?
- How big are point differences (close games vs blowouts)?

## Tech
Python • Pandas • Matplotlib • PyCharm

## Key insights
- Winning scores cluster around the high-20s/low-30s (e.g., 27, 31).
- Most games are decided by ~10–20 points; a few are major blowouts.
- Pitsburg Steelers and Patriots lead with most Super Bowl wins (6) 

## Visualizations
**Wins by Team**  
<img src="charts/wins_by_team.png" width="520">

**Common Winning Scores**  
<img src="charts/common_scores.png" width="520">

**Distribution of Point Differences**  
<img src="charts/point_diff.png" width="520">

## Reproduce
```bash
pip install pandas matplotlib
python main.py

