import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
