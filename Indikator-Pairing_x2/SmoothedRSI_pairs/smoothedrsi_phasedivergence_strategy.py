import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'PhaseDivergence': 1.0
        })
    )
