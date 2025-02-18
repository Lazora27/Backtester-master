import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DonchianVolatility': 1.0
        })
    )
