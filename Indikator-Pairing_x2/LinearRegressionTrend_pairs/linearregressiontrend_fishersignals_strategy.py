import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und FisherSignals
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'FisherSignals': 1.0
        })
    )
