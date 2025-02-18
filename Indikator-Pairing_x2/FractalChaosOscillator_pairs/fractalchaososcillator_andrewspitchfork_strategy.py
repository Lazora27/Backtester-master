import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
