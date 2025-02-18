import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
