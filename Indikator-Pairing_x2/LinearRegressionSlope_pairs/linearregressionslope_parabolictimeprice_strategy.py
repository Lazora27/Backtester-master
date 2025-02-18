import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
