import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'IntradayIntensity': 1.0
        })
    )
