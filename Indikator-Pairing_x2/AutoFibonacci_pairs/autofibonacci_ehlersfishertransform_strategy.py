import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
