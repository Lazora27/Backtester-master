import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
