import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
