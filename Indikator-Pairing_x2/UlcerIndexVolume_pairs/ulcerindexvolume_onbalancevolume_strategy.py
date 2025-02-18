import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
