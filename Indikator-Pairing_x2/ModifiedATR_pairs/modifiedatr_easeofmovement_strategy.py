import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'EaseOfMovement': 1.0
        })
    )
