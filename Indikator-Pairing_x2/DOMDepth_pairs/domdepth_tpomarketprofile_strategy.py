import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
