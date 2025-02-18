import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und DPOCycles
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'DPOCycles': 1.0
        })
    )
