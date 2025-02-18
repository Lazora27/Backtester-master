import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MurreyMathLines': 1.0
        })
    )
