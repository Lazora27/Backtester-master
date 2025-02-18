import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
