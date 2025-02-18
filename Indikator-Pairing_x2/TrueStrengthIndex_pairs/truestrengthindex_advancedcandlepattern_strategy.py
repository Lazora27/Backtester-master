import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
