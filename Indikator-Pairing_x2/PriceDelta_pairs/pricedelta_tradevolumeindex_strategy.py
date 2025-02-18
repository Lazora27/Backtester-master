import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
