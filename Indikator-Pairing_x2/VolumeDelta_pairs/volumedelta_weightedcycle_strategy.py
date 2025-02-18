import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'WeightedCycle': 1.0
        })
    )
