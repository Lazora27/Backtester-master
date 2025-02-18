import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'WeightedCycle': 1.0
        })
    )
