import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'IntradayIntensity': 1.0
        })
    )
