import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
