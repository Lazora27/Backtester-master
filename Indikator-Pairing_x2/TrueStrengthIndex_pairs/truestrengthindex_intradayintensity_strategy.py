import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
