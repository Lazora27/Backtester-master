import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ParabolicSAR': 1.0
        })
    )
