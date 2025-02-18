import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
