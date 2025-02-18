import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TPOMarketProfile_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TPOMarketProfile und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TPOMarketProfile': 1.0,
            'WeightedCycle': 1.0
        })
    )
