import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'MurreyMathLines': 1.0
        })
    )
