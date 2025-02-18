import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
