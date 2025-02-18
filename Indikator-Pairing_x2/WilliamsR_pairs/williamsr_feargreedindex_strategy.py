import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FearGreedIndex': 1.0
        })
    )
