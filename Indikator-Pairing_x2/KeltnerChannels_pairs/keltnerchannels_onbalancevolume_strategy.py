import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
