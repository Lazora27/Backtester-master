import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'KeltnerChannels': 1.0
        })
    )
