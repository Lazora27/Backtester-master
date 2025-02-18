import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
