import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
