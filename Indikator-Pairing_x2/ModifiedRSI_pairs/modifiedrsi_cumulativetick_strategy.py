import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'CumulativeTick': 1.0
        })
    )
