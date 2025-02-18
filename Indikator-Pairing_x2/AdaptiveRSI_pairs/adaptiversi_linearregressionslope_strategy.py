import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
