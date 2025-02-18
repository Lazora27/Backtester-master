import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
