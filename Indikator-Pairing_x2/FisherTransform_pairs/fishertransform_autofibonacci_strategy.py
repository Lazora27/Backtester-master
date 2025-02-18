import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AutoFibonacci': 1.0
        })
    )
