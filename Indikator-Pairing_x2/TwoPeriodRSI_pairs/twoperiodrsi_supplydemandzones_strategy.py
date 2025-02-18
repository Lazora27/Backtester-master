import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
