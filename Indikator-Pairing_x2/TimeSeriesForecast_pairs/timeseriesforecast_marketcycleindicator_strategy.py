import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
