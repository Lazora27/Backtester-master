import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
