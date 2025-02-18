import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
