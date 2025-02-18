import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'ModifiedATR': 1.0
        })
    )
