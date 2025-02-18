import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
