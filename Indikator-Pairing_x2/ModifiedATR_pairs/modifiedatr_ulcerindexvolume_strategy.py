import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
