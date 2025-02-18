import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ModifiedATR': 1.0
        })
    )
