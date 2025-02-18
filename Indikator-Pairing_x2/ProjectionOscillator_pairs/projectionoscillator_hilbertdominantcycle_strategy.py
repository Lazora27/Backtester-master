import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
