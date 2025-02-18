import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
