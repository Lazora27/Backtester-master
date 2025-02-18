import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
