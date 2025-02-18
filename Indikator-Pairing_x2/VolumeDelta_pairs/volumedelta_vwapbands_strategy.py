import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und VWAPBands
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'VWAPBands': 1.0
        })
    )
