import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
