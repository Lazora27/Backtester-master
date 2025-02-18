import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
