import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'CumulativeTick': 1.0
        })
    )
