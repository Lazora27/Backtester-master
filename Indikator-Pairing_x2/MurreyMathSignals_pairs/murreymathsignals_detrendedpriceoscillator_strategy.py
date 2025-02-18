import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_DetrendedPriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und DetrendedPriceOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'DetrendedPriceOscillator': 1.0
        })
    )
