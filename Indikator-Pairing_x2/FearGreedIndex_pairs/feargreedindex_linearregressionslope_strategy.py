import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
