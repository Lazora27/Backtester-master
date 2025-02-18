import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'BradleySiderograph': 1.0
        })
    )
