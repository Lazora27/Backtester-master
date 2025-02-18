import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
