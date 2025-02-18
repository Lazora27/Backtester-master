import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
