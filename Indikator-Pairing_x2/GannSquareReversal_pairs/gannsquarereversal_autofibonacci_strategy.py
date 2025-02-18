import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AutoFibonacci': 1.0
        })
    )
