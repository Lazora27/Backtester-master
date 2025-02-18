import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
