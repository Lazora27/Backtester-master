import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'EhlersDecycler': 1.0
        })
    )
