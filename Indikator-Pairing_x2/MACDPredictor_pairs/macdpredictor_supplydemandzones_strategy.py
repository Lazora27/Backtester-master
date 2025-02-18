import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
