import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
