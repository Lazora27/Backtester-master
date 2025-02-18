import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
