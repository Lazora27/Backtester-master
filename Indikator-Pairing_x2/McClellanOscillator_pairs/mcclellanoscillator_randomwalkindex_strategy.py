import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
