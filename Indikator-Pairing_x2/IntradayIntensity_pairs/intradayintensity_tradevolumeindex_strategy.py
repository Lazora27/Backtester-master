import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
