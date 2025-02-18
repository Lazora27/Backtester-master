import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
