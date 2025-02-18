import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
