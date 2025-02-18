import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
