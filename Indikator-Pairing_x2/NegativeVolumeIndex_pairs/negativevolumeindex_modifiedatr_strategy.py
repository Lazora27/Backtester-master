import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
