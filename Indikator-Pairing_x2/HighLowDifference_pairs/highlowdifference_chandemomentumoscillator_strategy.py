import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ChandeMomentumOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ChandeMomentumOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ChandeMomentumOscillator': 1.0
        })
    )
