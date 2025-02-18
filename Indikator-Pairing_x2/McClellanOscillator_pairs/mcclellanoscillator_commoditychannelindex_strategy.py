import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
