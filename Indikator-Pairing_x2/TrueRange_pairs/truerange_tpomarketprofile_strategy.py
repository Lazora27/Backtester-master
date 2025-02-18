import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
