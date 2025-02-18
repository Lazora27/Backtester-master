import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'TimeCycle': 1.0
        })
    )
