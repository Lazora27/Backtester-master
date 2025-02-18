import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
