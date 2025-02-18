import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'CumulativeTick': 1.0
        })
    )
