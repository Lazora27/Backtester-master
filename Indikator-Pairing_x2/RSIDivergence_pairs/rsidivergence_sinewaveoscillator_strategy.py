import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
