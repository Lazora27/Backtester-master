import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
