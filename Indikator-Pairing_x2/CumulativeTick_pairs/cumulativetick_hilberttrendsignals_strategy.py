import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
