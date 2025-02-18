import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
