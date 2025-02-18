import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VWAPBands
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VWAPBands': 1.0
        })
    )
