import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
