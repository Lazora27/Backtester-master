import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
