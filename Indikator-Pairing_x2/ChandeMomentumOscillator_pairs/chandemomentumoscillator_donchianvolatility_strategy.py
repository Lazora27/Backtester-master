import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeMomentumOscillator_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeMomentumOscillator und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ChandeMomentumOscillator': 1.0,
            'DonchianVolatility': 1.0
        })
    )
