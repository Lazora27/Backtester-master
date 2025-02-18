import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HistoricalATR': 1.0
        })
    )
