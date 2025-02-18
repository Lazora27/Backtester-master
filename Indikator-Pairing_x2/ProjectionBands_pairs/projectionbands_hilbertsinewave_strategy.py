import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'HilbertSinewave': 1.0
        })
    )
