import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'IntradayIntensity': 1.0
        })
    )
