import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'WeightedCycle': 1.0
        })
    )
