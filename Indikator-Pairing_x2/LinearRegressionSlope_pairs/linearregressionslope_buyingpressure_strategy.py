import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'BuyingPressure': 1.0
        })
    )
