import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
