import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'IntradayIntensity': 1.0
        })
    )
