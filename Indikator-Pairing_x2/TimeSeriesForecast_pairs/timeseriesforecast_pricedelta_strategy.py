import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und PriceDelta
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'PriceDelta': 1.0
        })
    )
