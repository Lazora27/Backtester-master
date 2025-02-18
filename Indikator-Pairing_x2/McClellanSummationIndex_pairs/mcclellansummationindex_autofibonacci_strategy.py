import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
