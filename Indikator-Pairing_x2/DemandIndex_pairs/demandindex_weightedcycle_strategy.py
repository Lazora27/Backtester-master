import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
