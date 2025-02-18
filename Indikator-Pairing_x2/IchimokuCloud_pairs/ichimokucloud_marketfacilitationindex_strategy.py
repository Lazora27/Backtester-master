import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
