import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
