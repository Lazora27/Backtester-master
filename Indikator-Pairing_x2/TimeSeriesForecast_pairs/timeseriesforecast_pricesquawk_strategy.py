import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'PriceSquawk': 1.0
        })
    )
