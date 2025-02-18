import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
