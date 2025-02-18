import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
