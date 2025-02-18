import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
