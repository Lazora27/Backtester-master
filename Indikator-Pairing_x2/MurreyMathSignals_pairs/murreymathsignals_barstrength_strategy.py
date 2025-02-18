import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und BarStrength
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'BarStrength': 1.0
        })
    )
