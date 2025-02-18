import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'HilbertTrendline': 1.0
        })
    )
