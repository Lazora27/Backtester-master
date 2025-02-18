import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
