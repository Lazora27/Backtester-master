import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
