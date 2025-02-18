import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'EhlersDecycler': 1.0
        })
    )
