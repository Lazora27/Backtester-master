import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'HullMovingAverage': 1.0
        })
    )
