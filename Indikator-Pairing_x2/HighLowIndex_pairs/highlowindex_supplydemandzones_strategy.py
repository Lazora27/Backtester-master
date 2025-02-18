import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
