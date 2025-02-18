import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VortexIndicator': 1.0
        })
    )
