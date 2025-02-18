import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
