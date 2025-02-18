import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
