import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'SeasonalStrength': 1.0
        })
    )
