import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
