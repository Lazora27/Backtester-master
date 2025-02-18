import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'PivotPoints': 1.0
        })
    )
