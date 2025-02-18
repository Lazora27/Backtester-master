import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
