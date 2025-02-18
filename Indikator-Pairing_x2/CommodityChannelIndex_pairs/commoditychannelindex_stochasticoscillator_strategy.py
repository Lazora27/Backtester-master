import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'StochasticOscillator': 1.0
        })
    )
