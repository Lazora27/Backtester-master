import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TrendCycles': 1.0
        })
    )
