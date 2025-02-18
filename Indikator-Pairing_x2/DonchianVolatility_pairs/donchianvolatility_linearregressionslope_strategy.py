import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
