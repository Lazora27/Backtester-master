import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
