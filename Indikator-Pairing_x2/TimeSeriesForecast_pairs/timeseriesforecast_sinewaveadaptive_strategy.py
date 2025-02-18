import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
