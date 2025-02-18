import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
