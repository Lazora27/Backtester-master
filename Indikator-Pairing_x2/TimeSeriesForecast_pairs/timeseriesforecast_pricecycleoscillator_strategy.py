import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
