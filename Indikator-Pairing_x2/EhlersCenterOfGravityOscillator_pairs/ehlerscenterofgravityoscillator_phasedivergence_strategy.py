import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersCenterOfGravityOscillator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersCenterOfGravityOscillator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'EhlersCenterOfGravityOscillator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
