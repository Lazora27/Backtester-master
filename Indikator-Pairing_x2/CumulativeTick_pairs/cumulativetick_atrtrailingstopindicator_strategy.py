import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ATRTrailingStopIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ATRTrailingStopIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ATRTrailingStopIndicator': 1.0
        })
    )
