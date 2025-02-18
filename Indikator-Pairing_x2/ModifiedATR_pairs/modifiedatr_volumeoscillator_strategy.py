import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'VolumeOscillator': 1.0
        })
    )
