import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
