import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'ExtensionProjections': 1.0
        })
    )
