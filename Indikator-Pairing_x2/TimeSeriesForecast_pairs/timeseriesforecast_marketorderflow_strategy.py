import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
