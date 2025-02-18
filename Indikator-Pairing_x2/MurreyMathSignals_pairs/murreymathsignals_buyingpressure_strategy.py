import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'BuyingPressure': 1.0
        })
    )
