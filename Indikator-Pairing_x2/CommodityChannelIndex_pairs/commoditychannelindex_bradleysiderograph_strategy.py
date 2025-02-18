import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
