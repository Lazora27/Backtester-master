import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
