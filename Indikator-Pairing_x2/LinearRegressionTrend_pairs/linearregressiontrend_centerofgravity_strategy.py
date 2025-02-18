import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'CenterOfGravity': 1.0
        })
    )
