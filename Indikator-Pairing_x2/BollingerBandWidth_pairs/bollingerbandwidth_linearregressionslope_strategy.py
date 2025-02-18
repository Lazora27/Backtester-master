import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
