import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
