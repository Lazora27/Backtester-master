import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'DonchianVolatility': 1.0
        })
    )
