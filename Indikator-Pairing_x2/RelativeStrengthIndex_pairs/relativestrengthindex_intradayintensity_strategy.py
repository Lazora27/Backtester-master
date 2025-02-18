import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
