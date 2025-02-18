import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
