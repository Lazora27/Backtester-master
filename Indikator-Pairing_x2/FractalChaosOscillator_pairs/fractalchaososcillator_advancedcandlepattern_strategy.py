import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
