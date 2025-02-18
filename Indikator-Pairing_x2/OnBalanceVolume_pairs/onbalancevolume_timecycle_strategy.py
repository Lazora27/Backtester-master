import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und TimeCycle
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'TimeCycle': 1.0
        })
    )
