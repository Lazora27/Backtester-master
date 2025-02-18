import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
