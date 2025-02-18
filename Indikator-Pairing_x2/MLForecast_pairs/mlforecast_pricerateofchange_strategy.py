import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
