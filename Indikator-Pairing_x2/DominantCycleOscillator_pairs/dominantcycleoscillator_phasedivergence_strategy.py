import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DominantCycleOscillator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DominantCycleOscillator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DominantCycleOscillator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
