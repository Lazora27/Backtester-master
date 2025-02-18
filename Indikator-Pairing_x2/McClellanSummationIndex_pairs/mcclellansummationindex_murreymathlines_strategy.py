import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
