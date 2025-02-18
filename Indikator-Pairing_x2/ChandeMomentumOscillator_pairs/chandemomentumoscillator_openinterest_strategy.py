import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeMomentumOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeMomentumOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ChandeMomentumOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
