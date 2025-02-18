import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
