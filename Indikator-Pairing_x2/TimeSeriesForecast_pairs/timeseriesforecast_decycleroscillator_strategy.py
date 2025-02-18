import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
