import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AccelerationBands': 1.0
        })
    )
