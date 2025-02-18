import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'SuperMACD': 1.0
        })
    )
