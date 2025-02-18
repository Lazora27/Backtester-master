import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'KeltnerChannels': 1.0
        })
    )
