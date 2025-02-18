import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
