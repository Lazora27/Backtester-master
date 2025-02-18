import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'VortexIndicator': 1.0
        })
    )
