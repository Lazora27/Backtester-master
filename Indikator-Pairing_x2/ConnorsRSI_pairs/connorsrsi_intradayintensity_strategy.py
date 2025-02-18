import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'IntradayIntensity': 1.0
        })
    )
