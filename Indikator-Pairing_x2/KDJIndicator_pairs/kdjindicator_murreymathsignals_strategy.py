import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
