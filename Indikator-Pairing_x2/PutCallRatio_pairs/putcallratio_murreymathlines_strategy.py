import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MurreyMathLines': 1.0
        })
    )
