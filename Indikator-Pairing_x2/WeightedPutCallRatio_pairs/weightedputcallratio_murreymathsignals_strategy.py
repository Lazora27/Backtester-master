import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
