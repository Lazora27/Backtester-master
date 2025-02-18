import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
