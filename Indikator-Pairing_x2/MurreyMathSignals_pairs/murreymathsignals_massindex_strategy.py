import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und MassIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'MassIndex': 1.0
        })
    )
