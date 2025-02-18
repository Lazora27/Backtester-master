import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
