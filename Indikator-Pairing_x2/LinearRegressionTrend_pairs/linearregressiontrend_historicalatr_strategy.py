import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'HistoricalATR': 1.0
        })
    )
