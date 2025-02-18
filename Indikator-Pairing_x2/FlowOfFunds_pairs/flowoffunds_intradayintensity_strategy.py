import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'IntradayIntensity': 1.0
        })
    )
