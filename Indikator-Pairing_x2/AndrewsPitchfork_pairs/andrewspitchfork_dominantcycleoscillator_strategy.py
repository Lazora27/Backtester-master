import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
