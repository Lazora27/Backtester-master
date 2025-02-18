import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
