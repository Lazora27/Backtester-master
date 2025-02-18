import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
