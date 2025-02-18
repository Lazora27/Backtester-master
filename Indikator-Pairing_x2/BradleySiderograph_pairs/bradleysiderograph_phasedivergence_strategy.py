import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'PhaseDivergence': 1.0
        })
    )
