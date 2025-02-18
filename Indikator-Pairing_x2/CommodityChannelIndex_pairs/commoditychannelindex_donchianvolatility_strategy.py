import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
