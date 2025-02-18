import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
