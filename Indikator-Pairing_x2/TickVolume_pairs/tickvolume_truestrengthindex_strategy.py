import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
