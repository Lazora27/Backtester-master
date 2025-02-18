import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
