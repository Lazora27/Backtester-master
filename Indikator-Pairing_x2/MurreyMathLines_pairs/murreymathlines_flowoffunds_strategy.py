import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'FlowOfFunds': 1.0
        })
    )
