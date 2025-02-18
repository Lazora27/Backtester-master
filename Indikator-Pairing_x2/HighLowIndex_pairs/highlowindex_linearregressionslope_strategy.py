import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
