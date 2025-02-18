import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'HilbertTrendline': 1.0
        })
    )
