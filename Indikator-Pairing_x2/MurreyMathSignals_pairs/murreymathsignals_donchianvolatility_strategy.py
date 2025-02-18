import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'DonchianVolatility': 1.0
        })
    )
