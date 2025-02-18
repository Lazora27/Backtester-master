import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'IntradayIntensity': 1.0
        })
    )
