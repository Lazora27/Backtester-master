import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
