import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TapeReading': 1.0
        })
    )
