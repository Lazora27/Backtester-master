import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
