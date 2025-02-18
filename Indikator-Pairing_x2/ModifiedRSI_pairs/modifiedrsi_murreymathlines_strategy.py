import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MurreyMathLines': 1.0
        })
    )
