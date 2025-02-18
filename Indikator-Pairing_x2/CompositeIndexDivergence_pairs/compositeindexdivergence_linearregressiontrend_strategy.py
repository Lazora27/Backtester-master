import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
