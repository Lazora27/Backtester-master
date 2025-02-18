import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
