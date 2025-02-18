import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PhaseDivergence': 1.0
        })
    )
