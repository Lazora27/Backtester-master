import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
