import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MurreyMathLines': 1.0
        })
    )
