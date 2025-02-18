import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
