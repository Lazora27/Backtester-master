import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
