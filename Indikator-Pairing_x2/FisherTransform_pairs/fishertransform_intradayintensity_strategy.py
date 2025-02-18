import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'IntradayIntensity': 1.0
        })
    )
