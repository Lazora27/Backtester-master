import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
