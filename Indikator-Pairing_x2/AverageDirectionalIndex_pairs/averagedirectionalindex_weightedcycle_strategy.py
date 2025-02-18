import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
