import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
