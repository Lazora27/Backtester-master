import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'IntradayIntensity': 1.0
        })
    )
