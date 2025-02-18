import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AutoFibonacci': 1.0
        })
    )
