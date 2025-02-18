import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
