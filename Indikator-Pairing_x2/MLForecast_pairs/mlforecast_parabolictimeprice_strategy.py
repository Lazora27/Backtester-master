import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
