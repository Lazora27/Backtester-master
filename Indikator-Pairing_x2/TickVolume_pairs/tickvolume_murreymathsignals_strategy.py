import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
