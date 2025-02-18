import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'VortexIndicator': 1.0
        })
    )
