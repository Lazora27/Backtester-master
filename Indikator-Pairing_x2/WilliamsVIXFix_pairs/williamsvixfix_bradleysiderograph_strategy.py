import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'BradleySiderograph': 1.0
        })
    )
