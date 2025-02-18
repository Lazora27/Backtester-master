import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
