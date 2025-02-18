import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
