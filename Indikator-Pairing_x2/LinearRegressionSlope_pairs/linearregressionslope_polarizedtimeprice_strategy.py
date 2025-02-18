import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
