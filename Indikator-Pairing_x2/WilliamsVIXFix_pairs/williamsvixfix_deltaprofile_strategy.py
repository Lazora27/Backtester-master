import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'DeltaProfile': 1.0
        })
    )
