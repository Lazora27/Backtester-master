import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
