import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
