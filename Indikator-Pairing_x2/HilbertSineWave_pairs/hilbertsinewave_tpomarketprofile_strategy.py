import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
