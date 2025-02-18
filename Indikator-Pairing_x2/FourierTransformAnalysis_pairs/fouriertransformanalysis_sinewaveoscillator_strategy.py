import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
