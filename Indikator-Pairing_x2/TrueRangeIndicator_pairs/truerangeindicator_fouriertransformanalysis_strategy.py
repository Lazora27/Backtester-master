import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
