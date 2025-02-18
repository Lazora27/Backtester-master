import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'BollingerBands': 1.0
        })
    )
