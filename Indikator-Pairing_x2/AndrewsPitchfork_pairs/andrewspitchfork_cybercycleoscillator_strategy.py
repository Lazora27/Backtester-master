import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
