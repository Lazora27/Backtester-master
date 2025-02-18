import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
