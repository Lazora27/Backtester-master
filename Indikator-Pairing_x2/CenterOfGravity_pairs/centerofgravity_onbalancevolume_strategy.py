import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
