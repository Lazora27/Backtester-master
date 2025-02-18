import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
