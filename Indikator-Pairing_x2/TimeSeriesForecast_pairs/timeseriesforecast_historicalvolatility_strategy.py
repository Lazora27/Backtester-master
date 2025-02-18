import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
