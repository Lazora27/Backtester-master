import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TickActivityIndex': 1.0
        })
    )
