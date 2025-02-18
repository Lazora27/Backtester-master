import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'FlowOfFunds': 1.0
        })
    )
