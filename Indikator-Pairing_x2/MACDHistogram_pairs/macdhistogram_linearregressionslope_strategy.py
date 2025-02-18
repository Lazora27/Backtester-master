import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
