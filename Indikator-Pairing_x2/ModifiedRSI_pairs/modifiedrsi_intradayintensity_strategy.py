import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'IntradayIntensity': 1.0
        })
    )
