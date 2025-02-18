import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'IntradayIntensity': 1.0
        })
    )
