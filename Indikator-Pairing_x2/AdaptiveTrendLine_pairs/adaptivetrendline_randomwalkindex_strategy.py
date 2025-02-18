import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
