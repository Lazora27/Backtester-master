import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
