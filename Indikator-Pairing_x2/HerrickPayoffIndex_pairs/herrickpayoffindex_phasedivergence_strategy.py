import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
