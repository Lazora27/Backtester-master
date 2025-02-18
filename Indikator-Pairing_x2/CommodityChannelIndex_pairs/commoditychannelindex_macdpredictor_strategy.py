import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'MACDPredictor': 1.0
        })
    )
