import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und FisherSignals
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'FisherSignals': 1.0
        })
    )
