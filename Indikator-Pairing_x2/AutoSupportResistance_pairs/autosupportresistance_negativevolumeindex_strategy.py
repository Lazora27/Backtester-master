import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
