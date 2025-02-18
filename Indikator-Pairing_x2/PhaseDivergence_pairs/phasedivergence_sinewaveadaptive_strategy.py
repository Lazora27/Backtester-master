import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
