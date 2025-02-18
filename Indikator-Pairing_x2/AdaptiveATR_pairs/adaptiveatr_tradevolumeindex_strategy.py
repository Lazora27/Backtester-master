import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
