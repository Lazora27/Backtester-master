import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
