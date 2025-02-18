import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MurreyMathLines': 1.0
        })
    )
