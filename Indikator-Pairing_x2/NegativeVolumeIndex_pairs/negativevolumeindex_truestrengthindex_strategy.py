import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
