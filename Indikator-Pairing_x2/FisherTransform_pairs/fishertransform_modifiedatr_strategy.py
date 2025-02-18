import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ModifiedATR': 1.0
        })
    )
