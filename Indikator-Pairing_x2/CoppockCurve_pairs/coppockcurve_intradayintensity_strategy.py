import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'IntradayIntensity': 1.0
        })
    )
