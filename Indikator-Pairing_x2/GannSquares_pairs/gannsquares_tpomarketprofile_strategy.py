import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
