import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
