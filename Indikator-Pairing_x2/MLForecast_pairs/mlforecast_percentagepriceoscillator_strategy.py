import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
