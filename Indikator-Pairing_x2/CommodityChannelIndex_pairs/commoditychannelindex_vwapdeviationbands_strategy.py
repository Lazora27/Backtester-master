import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
