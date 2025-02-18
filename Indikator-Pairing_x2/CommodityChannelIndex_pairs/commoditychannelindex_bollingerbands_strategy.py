import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
