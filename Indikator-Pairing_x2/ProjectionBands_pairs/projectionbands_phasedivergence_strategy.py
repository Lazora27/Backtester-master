import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'PhaseDivergence': 1.0
        })
    )
