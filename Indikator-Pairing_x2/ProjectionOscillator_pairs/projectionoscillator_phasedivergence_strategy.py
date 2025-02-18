import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
