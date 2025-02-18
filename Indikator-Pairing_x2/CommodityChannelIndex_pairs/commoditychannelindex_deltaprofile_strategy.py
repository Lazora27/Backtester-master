import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
