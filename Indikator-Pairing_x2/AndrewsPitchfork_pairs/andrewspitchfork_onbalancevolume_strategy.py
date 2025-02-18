import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
