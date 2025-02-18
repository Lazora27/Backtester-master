import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'UltimateOscillator': 1.0
        })
    )
