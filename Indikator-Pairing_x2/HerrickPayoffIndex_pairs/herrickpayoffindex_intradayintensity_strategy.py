import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
