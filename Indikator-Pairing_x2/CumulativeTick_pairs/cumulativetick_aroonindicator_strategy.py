import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AroonIndicator': 1.0
        })
    )
