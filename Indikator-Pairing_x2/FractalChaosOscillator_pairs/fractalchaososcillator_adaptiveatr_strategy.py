import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AdaptiveATR': 1.0
        })
    )
