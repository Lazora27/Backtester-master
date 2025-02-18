import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und TimeCycle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'TimeCycle': 1.0
        })
    )
