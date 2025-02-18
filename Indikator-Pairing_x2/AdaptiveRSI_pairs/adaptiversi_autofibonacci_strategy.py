import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AutoFibonacci': 1.0
        })
    )
