import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
