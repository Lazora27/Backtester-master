import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
