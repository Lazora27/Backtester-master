import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
