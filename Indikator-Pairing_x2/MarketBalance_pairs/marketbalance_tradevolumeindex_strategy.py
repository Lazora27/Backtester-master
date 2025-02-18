import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
