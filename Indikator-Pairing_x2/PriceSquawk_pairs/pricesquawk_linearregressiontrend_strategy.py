import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
