import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
