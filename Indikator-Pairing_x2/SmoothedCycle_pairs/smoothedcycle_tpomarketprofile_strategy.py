import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedCycle_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedCycle und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SmoothedCycle': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
