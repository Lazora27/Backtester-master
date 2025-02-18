import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
