import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
