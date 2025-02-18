import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'DeltaProfile': 1.0
        })
    )
