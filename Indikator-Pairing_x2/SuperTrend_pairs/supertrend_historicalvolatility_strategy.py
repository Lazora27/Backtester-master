import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
