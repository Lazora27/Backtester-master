import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
