import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'EhlersDecycler': 1.0
        })
    )
