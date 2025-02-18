import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
