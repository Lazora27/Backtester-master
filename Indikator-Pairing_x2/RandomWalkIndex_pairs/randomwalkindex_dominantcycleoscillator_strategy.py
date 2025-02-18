import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
