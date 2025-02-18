import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
