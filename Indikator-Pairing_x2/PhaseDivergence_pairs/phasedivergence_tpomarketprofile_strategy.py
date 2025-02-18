import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
