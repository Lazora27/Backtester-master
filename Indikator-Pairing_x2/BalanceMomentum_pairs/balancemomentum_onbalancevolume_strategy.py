import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
