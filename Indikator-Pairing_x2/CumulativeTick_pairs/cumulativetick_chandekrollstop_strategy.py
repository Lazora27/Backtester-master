import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
