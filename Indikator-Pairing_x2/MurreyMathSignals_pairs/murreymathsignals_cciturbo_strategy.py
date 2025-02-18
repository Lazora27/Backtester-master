import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'CCITurbo': 1.0
        })
    )
