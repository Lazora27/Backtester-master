import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
