import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
