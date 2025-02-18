import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
