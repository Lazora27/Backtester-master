import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ModifiedRSI': 1.0
        })
    )
