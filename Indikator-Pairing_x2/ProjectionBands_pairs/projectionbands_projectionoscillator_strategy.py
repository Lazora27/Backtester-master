import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
