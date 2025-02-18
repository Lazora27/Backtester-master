import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
