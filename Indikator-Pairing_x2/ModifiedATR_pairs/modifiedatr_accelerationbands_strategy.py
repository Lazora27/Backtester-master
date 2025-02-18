import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'AccelerationBands': 1.0
        })
    )
