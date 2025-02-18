import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'IchimokuCloud': 1.0
        })
    )
