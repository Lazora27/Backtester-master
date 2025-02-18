import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
