import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
