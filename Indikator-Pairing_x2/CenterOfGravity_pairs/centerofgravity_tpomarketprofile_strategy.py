import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
