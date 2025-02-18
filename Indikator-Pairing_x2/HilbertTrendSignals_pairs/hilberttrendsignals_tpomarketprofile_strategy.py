import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
