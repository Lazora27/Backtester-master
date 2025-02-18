import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
