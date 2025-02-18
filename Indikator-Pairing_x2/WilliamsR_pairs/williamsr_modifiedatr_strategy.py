import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ModifiedATR': 1.0
        })
    )
