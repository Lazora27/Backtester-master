import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
