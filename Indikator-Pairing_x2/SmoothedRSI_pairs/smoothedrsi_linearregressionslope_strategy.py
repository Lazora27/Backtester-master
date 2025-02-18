import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
