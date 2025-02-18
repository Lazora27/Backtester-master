import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AutoFibonacci': 1.0
        })
    )
