import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
