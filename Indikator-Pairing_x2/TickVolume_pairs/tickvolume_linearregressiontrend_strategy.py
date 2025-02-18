import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
