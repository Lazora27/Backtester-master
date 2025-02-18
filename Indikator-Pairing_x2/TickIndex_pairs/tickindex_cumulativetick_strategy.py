import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
