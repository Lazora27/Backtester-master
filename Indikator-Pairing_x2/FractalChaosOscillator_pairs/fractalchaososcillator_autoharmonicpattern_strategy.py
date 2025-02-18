import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
