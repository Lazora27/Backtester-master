import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
