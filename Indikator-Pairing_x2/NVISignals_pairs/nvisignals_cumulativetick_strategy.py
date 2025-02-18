import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CumulativeTick': 1.0
        })
    )
