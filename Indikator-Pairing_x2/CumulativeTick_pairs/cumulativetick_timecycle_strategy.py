import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TimeCycle': 1.0
        })
    )
