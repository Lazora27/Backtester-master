import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
