import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
