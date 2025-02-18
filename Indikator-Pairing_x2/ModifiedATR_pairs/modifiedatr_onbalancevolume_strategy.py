import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
