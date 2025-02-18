import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'SmoothedCycle': 1.0
        })
    )
