import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und DPOCycles
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'DPOCycles': 1.0
        })
    )
