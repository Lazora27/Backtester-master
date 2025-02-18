import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
