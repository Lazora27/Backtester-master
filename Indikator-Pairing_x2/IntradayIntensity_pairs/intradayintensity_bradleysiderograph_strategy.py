import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'BradleySiderograph': 1.0
        })
    )
