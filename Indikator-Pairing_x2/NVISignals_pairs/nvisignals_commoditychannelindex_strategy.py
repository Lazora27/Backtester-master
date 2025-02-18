import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
