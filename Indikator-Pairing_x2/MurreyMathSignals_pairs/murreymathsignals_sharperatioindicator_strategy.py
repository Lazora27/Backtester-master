import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
