import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
