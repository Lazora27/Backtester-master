import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AutoFibonacci': 1.0
        })
    )
