import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'IntradayIntensity': 1.0
        })
    )
