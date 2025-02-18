import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'WeeklyCycle': 1.0
        })
    )
