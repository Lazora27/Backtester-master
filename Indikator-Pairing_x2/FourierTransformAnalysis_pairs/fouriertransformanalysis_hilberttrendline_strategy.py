import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'HilbertTrendline': 1.0
        })
    )
