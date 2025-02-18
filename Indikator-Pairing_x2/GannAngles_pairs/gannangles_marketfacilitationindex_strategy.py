import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
