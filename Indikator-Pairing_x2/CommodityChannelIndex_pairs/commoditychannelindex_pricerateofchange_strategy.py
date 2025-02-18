import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
