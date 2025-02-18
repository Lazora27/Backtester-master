import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'GannSquareReversal': 1.0
        })
    )
