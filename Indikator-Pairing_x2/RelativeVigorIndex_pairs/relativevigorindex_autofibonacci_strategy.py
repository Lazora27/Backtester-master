import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
