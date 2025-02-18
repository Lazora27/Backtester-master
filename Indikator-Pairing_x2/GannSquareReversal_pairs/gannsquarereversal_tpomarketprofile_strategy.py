import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
