import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
