import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
