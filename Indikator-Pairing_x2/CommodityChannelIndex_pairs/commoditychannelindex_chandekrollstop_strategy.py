import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
