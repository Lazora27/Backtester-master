import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'ParabolicSAR': 1.0
        })
    )
