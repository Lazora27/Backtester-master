import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'CoppockCurve': 1.0
        })
    )
