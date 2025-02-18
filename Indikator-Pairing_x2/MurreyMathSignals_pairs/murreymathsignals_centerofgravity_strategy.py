import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'CenterOfGravity': 1.0
        })
    )
