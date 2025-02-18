import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
