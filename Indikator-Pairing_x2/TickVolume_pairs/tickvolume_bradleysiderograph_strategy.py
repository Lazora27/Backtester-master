import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BradleySiderograph': 1.0
        })
    )
