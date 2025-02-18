import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'MurreyMathLines': 1.0
        })
    )
