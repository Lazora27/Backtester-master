import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
