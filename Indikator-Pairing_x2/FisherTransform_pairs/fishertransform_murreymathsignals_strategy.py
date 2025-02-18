import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
