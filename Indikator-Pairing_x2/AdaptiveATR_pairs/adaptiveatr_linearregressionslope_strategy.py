import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
