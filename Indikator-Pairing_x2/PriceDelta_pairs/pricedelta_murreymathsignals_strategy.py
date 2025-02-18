import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
