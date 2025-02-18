import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
