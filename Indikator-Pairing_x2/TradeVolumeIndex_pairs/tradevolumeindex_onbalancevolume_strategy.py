import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
