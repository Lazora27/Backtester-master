import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
