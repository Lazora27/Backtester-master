import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
