import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
