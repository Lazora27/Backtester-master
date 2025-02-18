import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
