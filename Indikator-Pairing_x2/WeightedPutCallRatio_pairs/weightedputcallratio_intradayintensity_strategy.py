import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'IntradayIntensity': 1.0
        })
    )
