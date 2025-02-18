import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
