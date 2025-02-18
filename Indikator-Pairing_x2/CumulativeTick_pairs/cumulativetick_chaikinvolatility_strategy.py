import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
