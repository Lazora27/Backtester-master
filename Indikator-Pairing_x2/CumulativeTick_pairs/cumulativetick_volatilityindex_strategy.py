import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VolatilityIndex': 1.0
        })
    )
