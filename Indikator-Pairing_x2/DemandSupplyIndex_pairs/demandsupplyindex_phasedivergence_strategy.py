import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
