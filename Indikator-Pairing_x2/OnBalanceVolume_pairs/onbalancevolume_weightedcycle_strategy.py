import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'WeightedCycle': 1.0
        })
    )
