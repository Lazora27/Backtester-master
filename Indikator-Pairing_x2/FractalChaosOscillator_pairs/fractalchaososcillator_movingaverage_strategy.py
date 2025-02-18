import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'MovingAverage': 1.0
        })
    )
