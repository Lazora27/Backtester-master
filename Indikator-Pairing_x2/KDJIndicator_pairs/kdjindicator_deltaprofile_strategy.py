import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'DeltaProfile': 1.0
        })
    )
