import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
