import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
