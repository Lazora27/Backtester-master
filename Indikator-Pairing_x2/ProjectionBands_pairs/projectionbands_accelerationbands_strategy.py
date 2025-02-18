import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'AccelerationBands': 1.0
        })
    )
