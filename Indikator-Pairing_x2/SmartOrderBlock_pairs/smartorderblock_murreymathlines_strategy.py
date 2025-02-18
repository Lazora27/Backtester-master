import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'MurreyMathLines': 1.0
        })
    )
