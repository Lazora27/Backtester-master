import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
