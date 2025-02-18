import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PhaseDivergence': 1.0
        })
    )
