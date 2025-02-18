import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
