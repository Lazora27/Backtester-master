import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'WeightedCycle': 1.0
        })
    )
