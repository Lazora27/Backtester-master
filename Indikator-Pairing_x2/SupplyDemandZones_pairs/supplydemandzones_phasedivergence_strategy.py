import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'PhaseDivergence': 1.0
        })
    )
