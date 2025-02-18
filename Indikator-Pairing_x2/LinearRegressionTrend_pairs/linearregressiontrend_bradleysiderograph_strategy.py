import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'BradleySiderograph': 1.0
        })
    )
