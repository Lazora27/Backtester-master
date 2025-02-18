import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'WeightedCycle': 1.0
        })
    )
