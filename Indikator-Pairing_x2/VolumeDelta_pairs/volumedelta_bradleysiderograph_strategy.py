import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'BradleySiderograph': 1.0
        })
    )
