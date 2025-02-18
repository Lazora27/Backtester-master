import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
