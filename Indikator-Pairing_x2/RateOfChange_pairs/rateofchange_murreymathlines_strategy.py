import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MurreyMathLines': 1.0
        })
    )
