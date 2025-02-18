import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
