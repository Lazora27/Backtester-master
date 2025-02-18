import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'PhaseDivergence': 1.0
        })
    )
