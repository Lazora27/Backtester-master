import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertPhaseIndicator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertPhaseIndicator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HilbertPhaseIndicator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
