import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ConnorsRSI': 1.0
        })
    )
