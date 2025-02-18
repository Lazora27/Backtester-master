import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
