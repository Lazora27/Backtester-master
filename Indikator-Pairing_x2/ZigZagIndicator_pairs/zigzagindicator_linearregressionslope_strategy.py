import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
