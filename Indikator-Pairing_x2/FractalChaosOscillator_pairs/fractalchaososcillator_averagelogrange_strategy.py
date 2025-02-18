import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AverageLogRange': 1.0
        })
    )
