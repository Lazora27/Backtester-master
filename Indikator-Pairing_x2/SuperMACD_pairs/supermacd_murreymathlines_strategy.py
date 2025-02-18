import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MurreyMathLines': 1.0
        })
    )
