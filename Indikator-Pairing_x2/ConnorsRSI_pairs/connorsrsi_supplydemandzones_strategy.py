import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
