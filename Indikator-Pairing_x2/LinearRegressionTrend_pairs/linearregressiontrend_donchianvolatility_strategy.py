import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'DonchianVolatility': 1.0
        })
    )
