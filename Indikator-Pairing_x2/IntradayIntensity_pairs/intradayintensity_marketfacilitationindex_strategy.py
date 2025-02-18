import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
