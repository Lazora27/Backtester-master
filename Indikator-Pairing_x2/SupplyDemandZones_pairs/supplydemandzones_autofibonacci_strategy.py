import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AutoFibonacci': 1.0
        })
    )
