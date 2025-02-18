import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
