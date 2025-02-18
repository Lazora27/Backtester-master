import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
