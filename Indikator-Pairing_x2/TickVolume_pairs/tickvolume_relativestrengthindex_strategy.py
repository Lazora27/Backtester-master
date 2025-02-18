import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
