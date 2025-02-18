import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
