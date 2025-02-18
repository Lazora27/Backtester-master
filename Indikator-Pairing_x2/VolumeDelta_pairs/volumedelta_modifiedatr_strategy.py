import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ModifiedATR': 1.0
        })
    )
