import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und DemandIndex
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'DemandIndex': 1.0
        })
    )
