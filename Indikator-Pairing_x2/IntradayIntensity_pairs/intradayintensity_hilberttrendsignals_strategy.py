import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
