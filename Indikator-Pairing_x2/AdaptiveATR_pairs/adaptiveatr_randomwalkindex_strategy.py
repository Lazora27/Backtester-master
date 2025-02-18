import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
