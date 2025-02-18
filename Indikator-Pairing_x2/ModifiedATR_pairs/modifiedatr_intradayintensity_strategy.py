import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'IntradayIntensity': 1.0
        })
    )
