import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'SmoothedCycle': 1.0
        })
    )
