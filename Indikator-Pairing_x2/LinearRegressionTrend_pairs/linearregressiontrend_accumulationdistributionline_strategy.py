import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
