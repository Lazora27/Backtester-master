import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
