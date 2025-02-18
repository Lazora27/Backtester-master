import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'VolatilityIndex': 1.0
        })
    )
