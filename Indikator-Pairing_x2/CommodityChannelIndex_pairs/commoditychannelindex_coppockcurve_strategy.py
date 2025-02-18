import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
