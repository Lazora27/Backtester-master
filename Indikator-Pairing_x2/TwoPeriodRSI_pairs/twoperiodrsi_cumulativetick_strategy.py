import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'CumulativeTick': 1.0
        })
    )
