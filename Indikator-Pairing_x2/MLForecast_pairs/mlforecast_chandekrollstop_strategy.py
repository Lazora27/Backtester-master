import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
