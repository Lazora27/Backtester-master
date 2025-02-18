import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
