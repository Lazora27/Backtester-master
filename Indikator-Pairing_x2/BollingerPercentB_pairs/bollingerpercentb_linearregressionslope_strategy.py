import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
