import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
