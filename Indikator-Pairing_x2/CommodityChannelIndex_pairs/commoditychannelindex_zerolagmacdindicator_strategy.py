import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ZeroLagMACDIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ZeroLagMACDIndicator
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ZeroLagMACDIndicator': 1.0
        })
    )
