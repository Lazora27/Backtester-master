import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
