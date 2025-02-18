import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
