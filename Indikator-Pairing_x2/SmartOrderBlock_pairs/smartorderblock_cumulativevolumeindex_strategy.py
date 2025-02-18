import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CumulativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CumulativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CumulativeVolumeIndex': 1.0
        })
    )
