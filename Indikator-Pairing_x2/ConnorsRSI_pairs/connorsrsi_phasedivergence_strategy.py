import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'PhaseDivergence': 1.0
        })
    )
