import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
