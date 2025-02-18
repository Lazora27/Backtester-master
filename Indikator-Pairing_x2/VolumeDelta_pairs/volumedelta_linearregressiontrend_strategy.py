import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
