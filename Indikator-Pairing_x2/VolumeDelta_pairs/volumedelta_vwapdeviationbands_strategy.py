import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
