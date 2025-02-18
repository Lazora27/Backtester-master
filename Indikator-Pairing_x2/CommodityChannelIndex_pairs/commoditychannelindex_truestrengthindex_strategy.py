import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
